import speech_recognition as sr
from .speech_utils import speak, takeCommand
from .modules.youtube import play_youtube_music
import google.generativeai as genai
from googletrans import Translator
from .load_config import load_config

config = load_config()

modules = config["modules"]

genai.configure(api_key=config["keys"]["GOOGLE_AI_API_KEY"])
player = None

while True:
        query = takeCommand().lower()
        print(query)
        c = 0
        if config["name"] in query:
            req = query.replace(config["name"], "")
            if req.endswith("copy that") or req.endswith("copy"):
                req = req.replace("copy that", "")
                req = req.replace("copy", "")
                
            if modules.get("music") == True:
                if "play" in query:
                    c+=1
                    req = req.replace("play", "")
                    player = play_youtube_music(req)
                elif "volume up" in query:
                    c+=1
                    volume = player.audio_get_volume()
                    player.audio_set_volume(volume + 10)
                elif "volume full" in query:
                    c+=1
                    player.audio_set_volume(100)
                elif "volume down" in query:
                    c+=1
                    volume = player.audio_get_volume()
                    player.audio_set_volume(volume - 10)
                elif "pause" in query:
                    c+=1
                    player.pause()
                    speak("Playback paused.")
                elif "resume" in query:
                    c+=1
                    player.play()
                    speak("Playback resumed.")
                elif "stop" in query:
                    c+=1
                    speak("Playback stopped.")
                    player.stop()
            
            if c==0:
                print("Bruh thiswrking")
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(req + ". DO NOT USE FORMATTING AND ANSWER IN NORMAL HUMAN SPEECH")
                res = response.text
                print(res)
                if config["lang"] != "en":
                    langed = Translator().translate(res, src="en", dest=config["lang"])
                    speak(langed.text, config["lang"])
                else:
                    speak(res)