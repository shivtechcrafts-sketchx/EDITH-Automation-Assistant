from core.listener import listen
from core.intents import process_command
from core.speaker import speak
from config import WAKE_WORD

def run_assistant():
    speak("Hello Boss! your EDITH is online .")

    while True:
        command = listen()

        if WAKE_WORD in command:
            speak("Yes?")
            command = listen()
            process_command(command)