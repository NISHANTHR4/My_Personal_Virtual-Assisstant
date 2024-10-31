import requests
from speech_synthesis import speak

def tell_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    r = requests.get(url)
    if r.status_code == 200:
        joke = r.json()
        setup = joke['setup']
        punchline = joke['punchline']
        speak(f"Here is a joke: {setup} ... {punchline}")
    else:
        speak("Failed to fetch a joke")
