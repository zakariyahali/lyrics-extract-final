Lyrics Extractor and Image Generator Web Application

Project Description:
The Lyrics Extractor and Image Generator web application is a comprehensive tool designed to transform audio files into visual art. 
Leveraging advanced speech recognition and state-of-the-art AI models, this application allows users to upload MP3 files,
 transcribe the audio into text, summarize the content, and generate visually appealing images based on the summarized text.

####################################################################################################################
####################################################################################################################

Features:

1. MP3 to Text Transcription:
Users can upload MP3 files which are then converted to WAV format for processing.
The application uses Google's speech recognition to accurately transcribe the audio content into text.

2. Text Summarization:
After transcription, the full text is summarized into a concise, single-sentence description using OpenAI's GPT-3.5-turbo model.
This summary provides a clear and succinct representation of the audio content.


3. AI-Powered Image Generation:
The summarized text is used as a prompt to generate high-quality images using OpenAI's DALL-E model.
The generated images are visually aligned with the summarized content, offering a creative representation of the audio input.


4. User-Friendly Interface:
A clean and intuitive HTML interface allows users to easily upload files, select languages, and view results.
The application provides a seamless experience from audio upload to image generation.


5. Dynamic Feedback:
The application displays the transcribed text, the summarized content, and the generated image in a well-organized format.
Users receive immediate feedback on the transcription and image generation process.

####################################################################################################################
####################################################################################################################

## Technical Specifications: ##

Backend: Built with FastAPI, the backend handles file uploads, audio conversion, transcription, summarization, and image generation.

Frontend: The HTML frontend uses jQuery for dynamic content updates and form handling.

Speech Recognition: Utilizes the speech_recognition and pydub libraries for audio processing and transcription.

AI Integration: Employs OpenAI's API for both text summarization (using GPT-3.5-turbo) and image generation (using DALL-E).

File Handling: Ensures efficient management of uploaded and converted files, including automated cleanup after processing.

Environment Configuration: Uses python-dotenv to manage API keys and other configuration settings.


####################################################################################################################
####################################################################################################################

How It Works:
1. Upload: Users upload an MP3 file via the web interface.
2. Conversion: The application converts the MP3 file to WAV format.
3. Transcription: The audio content is transcribed into text using Google's speech recognition.
4. Summarization: The transcribed text is summarized into a concise description.
5. Image Generation: An image is generated based on the summarized text using OpenAI's DALL-E model.
6. Display: The full transcription, summary, and generated image are displayed on the web interface.

####################################################################################################################
####################################################################################################################
"""
This project exemplifies the power of combining speech recognition with advanced AI models to create a unique and engaging user experience. 
The resulting images offer a visual interpretation of audio content, opening new avenues for creativity and expression.
"""