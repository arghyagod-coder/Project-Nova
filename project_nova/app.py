# Speech utility functions
from .speech_utilities.capture_speech import takeCommand
from .speech_utilities.deliver_speech_tts import speak


# Main AI, models imports
from .core_functions.finetuned_gemini_call import get_gemini
from .core_functions.llama_call import process_command_with_ollama


# Other functions
from .other_functions import internet_status


# General
import os 
from dotenv import load_dotenv


load_dotenv()

Name = str(os.environ["Name"])

internet_access = internet_status()

while True:
        
        # query = takeCommand().lower()
        query = input("input: ")
        if Name.lower() in query:

            if not internet_access:
                response = get_gemini(query)
            else:
                 response = process_command_with_ollama(query)

            speak(response)

