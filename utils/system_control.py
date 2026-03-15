import os
from core.speaker import speak

def shutdown():
    speak("Shutting down system")
    os.system("shutdown /s /t 5")

def restart():
    speak("Restarting system")
    os.system("shutdown /r /t 5")

def get_system_info():
    import platform
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor()
    }
    return info

