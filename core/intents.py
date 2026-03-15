import os
import webbrowser
import datetime
import subprocess
import psutil
import pyautogui
import screen_brightness_control as sbc
from core.speaker import speak
from utils.web_control import search_google, search_youtube, open_google, open_youtube


# ---------------- GREETING ---------------- #

def greet():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Hey Boss! Good morning ! How can I assist you today?")
    elif 12 <= hour < 18:
        speak("Hey Boss! Good afternoon! What can I do for you?")
    else:
        speak("Hey Boss! Good evening! How may I help you?")


# ---------------- VOLUME CONTROL ---------------- #

def volume_up():
    pyautogui.press("volumeup")
    speak("Volume increased.")


def volume_down():
    pyautogui.press("volumedown")
    speak("Volume decreased.")


def mute_volume():
    pyautogui.press("volumemute")
    speak("Volume muted.")


# ---------------- BRIGHTNESS CONTROL ---------------- #

def brightness_up():
    current = sbc.get_brightness(display=0)[0]
    new = min(current + 10, 100)
    sbc.set_brightness(new)
    speak(f"Brightness set to {new} percent.")


def brightness_down():
    current = sbc.get_brightness(display=0)[0]
    new = max(current - 10, 0)
    sbc.set_brightness(new)
    speak(f"Brightness set to {new} percent.")


# ---------------- FILE & FOLDER ---------------- #

def create_folder(name):
    path = os.path.join(os.getcwd(), name)
    os.makedirs(path, exist_ok=True)
    speak(f"Folder {name} created.")


def search_file(filename, search_path="C:\\"):
    speak("Searching file. Please wait.")
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            speak(f"File found at {root}")
            os.startfile(root)
            return
    speak("File not found.")


# ---------------- SYSTEM ---------------- #

def shutdown():
    speak("Shutting down system.")
    os.system("shutdown /s /t 5")


def restart():
    speak("Restarting system.")
    os.system("shutdown /r /t 5")


# ---------------- APPS ---------------- #

def open_notepad():
    speak("Opening Notepad.")
    subprocess.Popen("notepad.exe")


def close_notepad():
    speak("Closing Notepad.")
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == "notepad.exe":
                proc.terminate()
        except:
            pass


def open_calculator():
    speak("Opening Calculator.")
    subprocess.Popen("calc.exe")


def close_calculator():
    speak("Closing Calculator.")
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() in ["calculator.exe", "applicationframehost.exe"]:
                proc.terminate()
        except:
            pass


def open_excel():
    speak("Opening Excel.")
    subprocess.Popen("excel.exe")
    


def close_excel():
    speak("Closing Excel.")
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == "excel.exe":
                proc.terminate()
        except:
            pass


def open_powerpoint():
    speak("Opening PowerPoint.")
    subprocess.Popen("powerpnt.exe")


def close_powerpoint():
    speak("Closing PowerPoint.")
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == "powerpnt.exe":
                proc.terminate()
        except:
            pass


# ---------------- TIME & DATE ---------------- #

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")


def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")


# ---------------- MAIN PROCESS ---------------- #

def process_command(command):
    command = command.lower().strip()

    # Greeting
    if "hello" in command or "hi edith" in command:
        greet()

    # ---------------- SMART WEB SEARCH ---------------- #

    # YouTube smart search
    elif "open youtube and search" in command:
        query = command.split("open youtube and search", 1)[1].strip()
        if query:
            speak(f"Searching YouTube for {query}")
            search_youtube(query)
        else:
            speak("What should I search on YouTube?")

    elif "search on youtube for" in command:
        query = command.split("search on youtube for", 1)[1].strip()
        if query:
            speak(f"Searching YouTube for {query}")
            search_youtube(query)
        else:
            speak("What should I search on YouTube?")

    elif "search youtube for" in command:
        query = command.split("search youtube for", 1)[1].strip()
        if query:
            speak(f"Searching YouTube for {query}")
            search_youtube(query)
        else:
            speak("What should I search on YouTube?")

    elif command.startswith("youtube "):
        query = command.replace("youtube", "", 1).strip()
        if query:
            speak(f"Searching YouTube for {query}")
            search_youtube(query)
        else:
            speak("Opening YouTube.")
            open_youtube()

    # Google smart search
    elif "open google and search" in command:
        query = command.split("open google and search", 1)[1].strip()
        if query:
            speak(f"Searching Google for {query}")
            search_google(query)
        else:
            speak("What should I search on Google?")

    elif "search on google for" in command:
        query = command.split("search on google for", 1)[1].strip()
        if query:
            speak(f"Searching Google for {query}")
            search_google(query)
        else:
            speak("What should I search on Google?")

    elif "search google for" in command:
        query = command.split("search google for", 1)[1].strip()
        if query:
            speak(f"Searching Google for {query}")
            search_google(query)
        else:
            speak("What should I search on Google?")

    elif command.startswith("google "):
        query = command.replace("google", "", 1).strip()
        if query:
            speak(f"Searching Google for {query}")
            search_google(query)
        else:
            speak("Opening Google.")
            open_google()

    # ---------------- VOLUME ---------------- #

    elif "raise the volume" in command or "volume up" in command:
        volume_up()

    elif "decrease volume" in command or "volume down" in command:
        volume_down()

    elif "mute" in command:
        mute_volume()

    # ---------------- BRIGHTNESS ---------------- #

    elif "brightness up" in command:
        brightness_up()

    elif "brightness down" in command:
        brightness_down()

    # ---------------- FILE & FOLDER ---------------- #

    elif "create folder" in command:
        speak("What should I name the folder?")
        from core.listener import listen
        name = listen()
        if name:
            create_folder(name)

    elif "search file" in command:
        speak("Tell me the file name.")
        from core.listener import listen
        filename = listen()
        if filename:
            search_file(filename)

    # ---------------- APPS ---------------- #

    elif "open powerpoint" in command:
        open_powerpoint()

    elif "close powerpoint" in command:
        close_powerpoint()

    elif "open excel" in command:
        open_excel()

    elif "close excel" in command:
        close_excel()

    elif "open notepad" in command:
        open_notepad()

    elif "close notepad" in command:
        close_notepad()

    elif "open calculator" in command:
        open_calculator()

    elif "close calculator" in command:
        close_calculator()

    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "close github" in command:
        speak("Closing GitHub.")
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "chrome.exe":
                    proc.terminate()
            except:
                pass

    elif "open linkedin" in command:
        speak("Opening LinkedIn.")
        webbrowser.open("https://linkedin.com")

    elif "close linkedin" in command:
        speak("Closing LinkedIn.")
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "chrome.exe":
                    proc.terminate()
            except:
                pass

    elif "open website" in command:
        speak("Which website should I open?")
        from core.listener import listen
        site = listen()
        if site:
            url = f"https://{site.replace(' ', '')}.com"
            speak(f"Opening {site}.")
            webbrowser.open(url)

    elif "open file explorer" in command:
        speak("Opening File Explorer.")
        subprocess.Popen("explorer.exe")

    elif "close file explorer" in command:
        speak("Closing File Explorer.")
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "explorer.exe":
                    proc.terminate()
            except:
                pass

    elif "open command prompt" in command:
        speak("Opening Command Prompt.")
        subprocess.Popen("cmd.exe")

    elif "close command prompt" in command:
        speak("Closing Command Prompt.")
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "cmd.exe":
                    proc.terminate()
            except:
                pass

    elif "open task manager" in command:
        speak("Opening Task Manager.")
        subprocess.Popen("taskmgr.exe")

    elif "close task manager" in command:
        speak("Closing Task Manager.")
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "taskmgr.exe":
                    proc.terminate()
            except:
                pass

    # ---------------- WEB ---------------- #

    elif "open youtube" in command:
        speak("Opening YouTube.")
        open_youtube()

    elif "close youtube" in command:
        speak("Closing YouTube.")
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "chrome.exe":
                    proc.terminate()
            except:
                pass

    elif "open google" in command:
        speak("Opening Google.")
        open_google()

    elif "close google" in command:
        speak("Closing Google.")
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == "chrome.exe":
                    proc.terminate()
            except:
                pass

    # ---------------- TIME & DATE ---------------- #

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    # ---------------- SYSTEM ---------------- #

    elif "shutdown" in command:
        shutdown()

    elif "restart" in command:
        restart()

    elif "exit" in command or "stop" in command:
        speak("Going offline. Take care.")
        exit()

    else:
        speak("I did not understand that command.")