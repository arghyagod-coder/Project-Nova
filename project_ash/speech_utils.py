import subprocess
import pyttsx3
import speech_recognition as sr
# This project uses the external package flite for text to speech
def speak(ctx):
    subprocess.Popen(["/usr/bin/flite", "--setf", "duration_stretch=1.2", "-voice", "slt", ctx])


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
        query = r.recognize_tensorflow(audio, duration=10, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
    
    return query