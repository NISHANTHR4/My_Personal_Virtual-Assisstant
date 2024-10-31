import requests
from speech_synthesis import speak

def fetch_and_speak_weather(city):
    api_key = "6bf4bbrknbr561wkmdkeki"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        speak(f"The current temperature in {city} is {temp} degrees Celsius with {description}")
    else:
        speak(f"Failed to fetch weather for {city}")
