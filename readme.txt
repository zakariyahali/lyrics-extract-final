Project Description: Lyrics Extractor and Image Generator
Overview
The Lyrics Extractor and Image Generator is a web-based application that allows users to upload an MP3 file, extract the lyrics from it using Google's speech recognition API, and then generate an AI-inspired image based on the extracted lyrics using OpenAI's API. This project is built with FastAPI for the backend and a simple HTML frontend for user interaction.

Features
MP3 to WAV Conversion: The application converts uploaded MP3 files to WAV format for processing.
Lyrics Extraction: Extracts lyrics from the uploaded audio file using Google's speech recognition API.
Language Support: Supports multiple languages for lyrics extraction including English, Russian, and Spanish.
AI Image Generation: Generates an image inspired by the extracted lyrics using OpenAI's image generation API.
User-Friendly Interface: Provides a simple and clean web interface for uploading files, selecting languages, and displaying results.
Project Structure
.env: Contains environment variables like the OpenAI API key.
main.py: The main FastAPI application file handling routes and business logic.
requirements.txt: Lists all the dependencies required for the project.
uploads/: Directory to save uploaded MP3 files.
media/: Directory to save generated images.
static/: Directory for static files like CSS and JavaScript.
templates/: Directory for HTML templates, including the main index.html.
Dependencies
FastAPI: For building the backend API.
Uvicorn: ASGI server for running the FastAPI app.
Httpx: For making HTTP requests.
Pydub: For audio file manipulation.
SpeechRecognition: For transcribing audio files to text.
Python-dotenv: For loading environment variables.
Pillow: For image processing.
Requests: For making HTTP requests to the OpenAI API.
Jinja2: For rendering HTML templates.
Watchdog: For monitoring file system events.
How It Works
User Interaction:

The user uploads an MP3 file through the web interface.
The user selects the language for lyrics extraction.
Backend Processing:

The uploaded MP3 file is saved in the uploads/ directory.
The MP3 file is converted to WAV format.
The WAV file is transcribed to text using Google's speech recognition API.
The extracted lyrics are sent to the frontend and displayed to the user.
AI Image Generation:

The extracted lyrics are reformatted and sent to OpenAI's image generation API.
The generated image is saved in the media/ directory and displayed to the user.
Usage
Clone the repository.
Set up a virtual environment and install dependencies using pip install -r requirements.txt.
Create a .env file and add your OpenAI API key.
Run the FastAPI app using uvicorn main:app --reload.
Open a web browser and navigate to http://127.0.0.1:8000/ to use the application.
Example Workflow
User uploads an MP3 file of a song.
The backend converts the MP3 file to WAV format.
Google's speech recognition API extracts the lyrics from the WAV file.
The extracted lyrics are displayed on the web page.
The lyrics are sent to OpenAI's API to generate an image.
The generated image is displayed on the web page.
This project combines the capabilities of audio processing, speech recognition, and AI-based image generation to create a seamless and interactive experience for users.






########################################################################################################################################################
########################################################################################################################################################


How to install ffmpeg → 

Let's go through a more detailed guide to ensure FFmpeg is added correctly to the PATH on Windows 11:

### **Steps to Add FFmpeg to PATH on Windows 11**

1. **Download and Extract FFmpeg:**
    - Download the "essentials" build of FFmpeg from gyan.dev.
    - Extract the downloaded zip file to a location on your computer, e.g., **`C:\ffmpeg`**.
    - Ensure the extracted folder contains the **`bin`** directory with **`ffmpeg.exe`**, **`ffplay.exe`**, and **`ffprobe.exe`**.
2. **Open Environment Variables:**
    - Press **`Win + S`**, type **`Environment Variables`**, and select "Edit the system environment variables."
    - In the System Properties window, click on the "Environment Variables" button.
3. **Edit the Path Variable:**
    - In the Environment Variables window, under the "System variables" section, find the variable named **`Path`**. Select it and click "Edit".
4. **Add the FFmpeg Bin Directory to the Path:**
    - In the Edit Environment Variable window, click "New" and add the path to the **`bin`** directory of the extracted FFmpeg folder. For example:
        
        ```makefile
        makefileCopy code
        C:\ffmpeg\bin
        
        ```
        
    - Click "OK" to close all windows.

### **Verify FFmpeg Installation**

1. **Open a New Command Prompt or PowerShell Window:**
    - Press **`Win + S`**, type **`cmd`** or **`powershell`**, and press **`Enter`**.
2. **Check FFmpeg Version:**
    - Run the following command to verify that FFmpeg is correctly installed and accessible from any location:
        
        ```bash
        bashCopy code
        ffmpeg -version
        
        ```
        
    - If FFmpeg is correctly added to your PATH, you should see version information output.

### **Troubleshooting**

If the steps above do not work, ensure the following:

1. **Correct Path:**
    - Verify that the path added to the **`Path`** variable points directly to the **`bin`** directory where **`ffmpeg.exe`** is located. The full path should look something like **`C:\ffmpeg\bin`**.
2. **Environment Variable Changes:**
    - Sometimes, changes to environment variables require restarting the Command Prompt or PowerShell. Ensure any Command Prompt or PowerShell windows are closed and reopened after making the changes.
3. **Windows Restart:**
    - In some cases, restarting your computer can ensure that the changes take effect.
4. **Path Length Limit:**
    - Ensure the PATH variable does not exceed the system path length limit. If it does, remove some unnecessary paths or consider using a different method to add FFmpeg to your PATH.

By following these detailed steps, you should be able to resolve the issue and ensure that FFmpeg is correctly added to your PATH on Windows 11. If the problem persists, feel free to share specific error messages or issues you encounter.


