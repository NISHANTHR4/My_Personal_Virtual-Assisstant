import speech_recognition as sr
from speech_recognition_module import listen_for_wake_word, listen_for_command
from speech_synthesis import speak
from web_commands import process_web_command
from news_fetcher import fetch_and_speak_news
from wikipedia_fetcher import fetch_wikipedia_summary

recognizer = sr.Recognizer()

if __name__ == "__main__":
    speak("Initializing Nishanth....")
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            while True:
                print("Listening for 'Nishanth'...")
                word = listen_for_wake_word(recognizer, source)
                if word and word.lower() == "nishanth":
                    speak("Yes?")
                    print("Listening for command...")
                    command = listen_for_command(recognizer, source)
                    if command:
                        command = command.strip()
                        if "who is" in command.lower() or "what is" in command.lower():
                            summary = fetch_wikipedia_summary(command)
                            speak(summary)
                        else:
                            process_web_command(command)
                    else:
                        speak("Sorry, I didn't catch that.")
    except Exception as e:
        print(f"Error: {e}")
