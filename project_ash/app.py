import speech_recognition as sr
from .speech_utils import speak, takeCommand

def start():
    while True:
        query = takeCommand().lower()