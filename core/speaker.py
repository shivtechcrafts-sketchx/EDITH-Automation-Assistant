from gtts import gTTS
import pygame
import os
import uuid


pygame.mixer.init()


def speak(text):
    print("EDITH:", text)

    filename = f"temp_{uuid.uuid4()}.mp3"

    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    os.remove(filename)