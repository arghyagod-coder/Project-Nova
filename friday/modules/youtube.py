# import playsound as ps
import os
import yt_dlp
import subprocess
from ..speech_utils import speak
import vlc 


tmp_songfile_path = os.path.join(os.path.expanduser('~'), "FRIDAY", "tmp", "csong.wav")

def play_youtube_music(url):
    if os.path.exists(tmp_songfile_path):
        os.remove(tmp_songfile_path)
    else:
        print("Existing file does not exist") 
        
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': tmp_songfile_path}) as video:
        info_dict = video.extract_info(f"ytsearch:{url} song", download = True)
        video_title = info_dict['title']
        
        print(video_title)
        print("Successfully Downloaded - see local folder tmp/")
        speak("Playing {}".format(video_title))
        
        player = vlc.MediaPlayer(tmp_songfile_path)
        player.audio_set_volume(100)
        player.play()
        return player
        
        