import threading
from core.listener import listen
from core.intents import process_command
from core.speaker import speak
from gui.iron_hud import start_hud


def assistant_loop():
    speak("EDITH online and ready.")

    while True:
        command = listen()
        if not command:
            continue
        print("You:", command)
        process_command(command)


if __name__ == "__main__":
    assistant_thread = threading.Thread(target=assistant_loop)
    assistant_thread.daemon = True
    assistant_thread.start()

    # GUI MUST RUN IN MAIN THREAD
    start_hud()