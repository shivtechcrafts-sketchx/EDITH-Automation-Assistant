import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        command = recognizer.recognize_google(audio, language="en-IN")
        return command.lower()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        print("Could not understand.")
        return ""

    except sr.RequestError as e:
        print("API error:", e)
        return ""

    except Exception as e:
        print("Unexpected error:", e)
        return ""