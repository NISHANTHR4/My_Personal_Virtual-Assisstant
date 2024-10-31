import requests
from speech_synthesis import speak

def fetch_and_speak_news():
    api_key = "23c8dcddc09c4066bf9fa1770fb0b9b0"
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
    if r.status_code == 200:
        data = r.json()
        articles = data.get('articles', [])
        for article in articles:
            speak(article['title'])
    else:
        speak("Failed to fetch news")
