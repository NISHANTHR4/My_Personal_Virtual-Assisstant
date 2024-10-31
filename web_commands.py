import webbrowser
from speech_synthesis import speak
from news_fetcher import fetch_and_speak_news
from weather import fetch_and_speak_weather
from jokes import tell_joke
from time_date import tell_time, tell_date

musicLibrary = {
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "march": "https://www.youtube.com/watch?v=Xqeq4b5u_Xw",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D",
    "wolf": "https://www.youtube.com/watch?v=ThCH0U6aJpU&list=PLnrGi_-oOR6wm0Vi-1OsiLiV5ePSPs9oF&index=21"
}

def process_web_command(c):
    c_lower = c.lower()
    if "open google" in c_lower:
        webbrowser.open("https://google.com")
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c_lower:
        webbrowser.open("https://linkedin.com")
    elif c_lower.startswith("play"):
        song = c_lower.split(" ")[1]
        link = musicLibrary.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't know the song {song}")
    elif "news" in c_lower:
        fetch_and_speak_news()
    elif "weather" in c_lower:
        city = c_lower.replace("weather", "").strip()
        fetch_and_speak_weather(city)
    elif "joke" in c_lower:
        tell_joke()
    elif "time" in c_lower:
        tell_time()
    elif "date" in c_lower:
        tell_date()
    else:
        speak("Command not recognized")
