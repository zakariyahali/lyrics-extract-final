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
import requests

# Load environment variables
load_dotenv()

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

# Models
class LyricsPayload(BaseModel):
    lyrics: str

# Helper functions
def convert_mp3_to_wav(mp3_path, wav_path):
    """Convert MP3 file to WAV format."""
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
    logging.info(f"Converted MP3 to WAV: {wav_path}")

def transcribe_audio_to_text(wav_path, language='en-US'):
    """Transcribe audio file to text using Google's speech recognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            logging.error("Could not understand the audio")
            return "Sorry, could not understand the audio."
        except sr.RequestError as e:
            logging.error(f"Recognition request failed: {e}")
            return f"Could not request results; {e}"

def extract_lyrics_from_mp3(mp3_path, language='en-US'):
    """Extract lyrics from an MP3 file."""
    # Define paths
    wav_path = mp3_path.replace(".mp3", ".wav")
    
    # Convert MP3 to WAV
    convert_mp3_to_wav(mp3_path, wav_path)

    # Transcribe audio to text
    if os.path.exists(wav_path):
        lyrics = transcribe_audio_to_text(wav_path, language)
        os.remove(wav_path)  # Clean up the WAV file after processing
        return lyrics
    else:
        return "Failed to convert MP3 to WAV."

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

    # Extract lyrics from the uploaded file
    lyrics = extract_lyrics_from_mp3(file_location, language)
    return {"lyrics": lyrics}

@app.post("/reformat_lyrics/")
async def reformat_lyrics(payload: LyricsPayload):
    lyrics = payload.lyrics
    formatted_lyrics = lyrics.replace("\n", " ").strip()
    return {"formatted_lyrics": formatted_lyrics}

@app.post("/generate_image/")
async def generate_image(payload: LyricsPayload):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="API key not found.")
        
        chatgpt_url = "https://api.openai.com/v1/images/generations"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": payload.lyrics,
            "size": "1024x1024",
            "n": 1
        }
        
        response = requests.post(chatgpt_url, headers=headers, json=data)
        response.raise_for_status()
        
        image_url = response.json()['data'][0]['url']
        
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        image = Image.open(BytesIO(image_response.content))
        if not os.path.exists("media"):
            os.makedirs("media")
        image_path = os.path.join("media", "generated_image.png")
        image.save(image_path)
        
        return {"image_path": image_path}
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/media/generated_image.png")
async def get_generated_image():
    return FileResponse("media/generated_image.png")
