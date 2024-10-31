from datetime import datetime
from speech_synthesis import speak

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def tell_date():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    speak(f"Today's date is {current_date}")
