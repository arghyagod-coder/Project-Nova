import speech_recognition as sr
from .speech_utils import speak, takeCommand
import os 
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_AI_API_KEY"])


while True:
        query = takeCommand().lower()
        
        if "friday" in query:
            req = query.replace("friday", "")
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(req)
            speak(response.text)