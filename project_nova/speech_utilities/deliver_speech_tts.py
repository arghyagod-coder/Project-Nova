import subprocess
import pyttsx3

# This project uses the external package flite for text to speech
def speak(ctx):
    subprocess.Popen(["/usr/bin/flite", "-voice", "slt", ctx])


engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 0.9)

def alt_speak(ctx):    
    engine.say(ctx)
    engine.runAndWait()