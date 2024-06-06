from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os
from io import BytesIO
from pydub import AudioSegment
from PIL import Image
from dotenv import load_dotenv
import logging
import speech_recognition as sr
import openai
import requests

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory="templates")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure the converted_files directory exists
if not os.path.exists('converted_files'):
    os.makedirs('converted_files')

# Models
class LyricsPayload(BaseModel):
    lyrics: str

# Helper functions
def convert_mp3_to_wav(mp3_path, wav_path):
    """Convert MP3 file to WAV format."""
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
    logging.info(f"Converted MP3 to WAV: {wav_path}")

def split_audio(wav_path, chunk_length_ms=60000):
    """Split audio file into chunks of specified length (default is 60 seconds)."""
    audio = AudioSegment.from_wav(wav_path)
    chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

def transcribe_audio_chunk(chunk, chunk_index):
    """Transcribe a single audio chunk using OpenAI's API."""
    chunk_path = f"chunk_{chunk_index}.wav"
    chunk.export(chunk_path, format="wav")

    try:
        with open(chunk_path, 'rb') as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
            text = response['text']
    except Exception as e:
        logging.error(f"An error occurred with chunk {chunk_index}: {e}")
        text = ""
    finally:
        os.remove(chunk_path)  # Clean up the chunk file after processing
    return text

def transcribe_wav_to_text(wav_path):
    """Transcribe WAV file to text using OpenAI's API by splitting into chunks."""
    chunks = split_audio(wav_path)
    full_text = ""
    
    for i, chunk in enumerate(chunks):
        chunk_text = transcribe_audio_chunk(chunk, i)
        full_text += chunk_text + " "
    
    logging.info(f"Transcribed Text: {full_text.strip()}")
    return full_text.strip()

async def summarize_text(text):
    """Summarize the transcribed text using OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text in one sentence: {text}"}
            ]
        )
        summary = response.choices[0].message['content'].strip()
        logging.info(f"Generated summary: {summary}")
        return summary
    except Exception as e:
        logging.error(f"An error occurred during text summarization: {e}")
        return "Summary generation failed."


# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), language: str = Form(...)):
    # Ensure the uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    # Save the uploaded file
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    # Convert MP3 to WAV
    wav_file_location = f"converted_files/{file.filename.replace('.mp3', '.wav')}"
    convert_mp3_to_wav(file_location, wav_file_location)

    # Extract lyrics from the converted WAV file
    lyrics = transcribe_wav_to_text(wav_file_location)
    
    # Clean up the uploaded MP3 file
    os.remove(file_location)

    # Summarize the transcribed text
    summary = await summarize_text(lyrics)
    
    return {"lyrics": lyrics, "summary": summary}

@app.post("/generate_image/")
async def generate_image(payload: LyricsPayload):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logging.error("API key not found.")
            raise HTTPException(status_code=500, detail="API key not found.")
        
        dalle_url = "https://api.openai.com/v1/images/generations"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = f"Generate an image based on this text summary: {payload.lyrics}"
        if len(prompt) > 1000:
            prompt = prompt[:1000]  # Truncate the prompt if it's longer than 1000 characters
        
        data = {
            "prompt": prompt,
            "size": "1024x1024",
            "n": 1
        }
        
        logging.info(f"Sending request to OpenAI API with data: {data}")
        response = requests.post(dalle_url, headers=headers, json=data)
        logging.info(f"OpenAI API response status: {response.status_code}")
        logging.info(f"OpenAI API response content: {response.text}")
        response.raise_for_status()
        
        image_url = response.json()['data'][0]['url']
        
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        image = Image.open(BytesIO(image_response.content))
        if not os.path.exists("media"):
            os.makedirs("media")
        image_path = os.path.join("media", "generated_image.png")
        image.save(image_path)
        
        logging.info(f"Image saved at: {image_path}")
        return {"image_path": image_path}
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Request exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/media/generated_image.png")
async def get_generated_image():
    return FileResponse("media/generated_image.png")