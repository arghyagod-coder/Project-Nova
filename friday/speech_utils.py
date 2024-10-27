import subprocess
import pyttsx3
import speech_recognition as sr
from .load_config import load_config

config = load_config()

# This project uses the external package flite for text to speech
def speak(ctx):
    subprocess.Popen([config["speech"]["engine"], "-voice", config["speech"]["voice"], ctx])


engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 0.9)

def alt_speak(ctx):    
    engine.say(ctx)
    engine.runAndWait()
    
def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
    
    return query