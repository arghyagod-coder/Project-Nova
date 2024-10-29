import subprocess
import pyttsx3
import speech_recognition as sr
from .load_config import load_config

from gtts import gTTS
import vlc


config = load_config()

# This project uses the external package flite for text to speech
def speak_offline(ctx):
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

def speak(ctx, lang="en"):
    speech = gTTS(text = ctx, lang = lang, slow = False)
    mp3_file = '/home/jay/FRIDAY/tmp/speech.mp3'
    speech.save(mp3_file)
    player = vlc.MediaPlayer(mp3_file)
    player.audio_set_volume(100)
    player.play()
    return player

a = speak("bruh")