import pygame
from PIL import Image, ImageSequence
import os
from config import WINDOW_SIZE


def load_gif_frames(path):
    gif = Image.open(path)
    frames = []

    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")

        pygame_image = pygame.image.fromstring(
            frame.tobytes(),
            frame.size,
            "RGBA"
        )

        frames.append(pygame_image)

    print("Total frames loaded:", len(frames))
    return frames


def run_gui():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("EDITH AI")

    base_path = os.path.dirname(os.path.dirname(__file__))
    gif_path = os.path.join(base_path, "gui", "assets", "edith.gif")

    frames = load_gif_frames(gif_path)

    if len(frames) <= 1:
        print("⚠ GIF animated nahi hai ya sirf 1 frame hai.")

    clock = pygame.time.Clock()
    frame_index = 0

    running = True
    while running:
        screen.fill((0, 0, 0))

        current_frame = pygame.transform.scale(
            frames[frame_index],
            WINDOW_SIZE
        )

        screen.blit(current_frame, (0, 0))

        frame_index = (frame_index + 1) % len(frames)

        pygame.display.flip()
        clock.tick(15)  # 15 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()