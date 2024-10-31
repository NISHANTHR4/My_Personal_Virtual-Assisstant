import speech_recognition as sr

def listen_for_wake_word(recognizer, source):
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def listen_for_command(recognizer, source):
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
