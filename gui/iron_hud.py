import pygame
import math
import random
import sys
from datetime import datetime

# =========================
# INIT
# =========================
pygame.init()
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EDITH AI - Iron HUD Interface")
clock = pygame.time.Clock()

# =========================
# COLORS
# =========================
BG = (4, 8, 18)
DARK_BLUE = (10, 18, 35)
CYAN = (0, 255, 255)
SOFT_CYAN = (80, 220, 255)
BLUE = (0, 140, 255)
GLOW_BLUE = (0, 180, 255)
WHITE = (220, 240, 255)
RED = (255, 70, 70)
GREEN = (0, 255, 170)
YELLOW = (255, 220, 70)
PURPLE = (160, 80, 255)

# =========================
# FONTS
# =========================
font_small = pygame.font.SysFont("consolas", 18)
font_medium = pygame.font.SysFont("consolas", 26)
font_large = pygame.font.SysFont("consolas", 42, bold=True)
font_xl = pygame.font.SysFont("consolas", 64, bold=True)

# =========================
# HELPERS
# =========================
def draw_text(text, font, color, x, y, center=False):
    surf = font.render(text, True, color)
    rect = surf.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surf, rect)

def draw_glow_circle(surface, color, pos, radius, glow_layers=5):
    x, y = pos
    for i in range(glow_layers, 0, -1):
        alpha = max(10, 40 - i * 6)
        glow_surf = pygame.Surface((radius*4, radius*4), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (*color, alpha), (radius*2, radius*2), radius + i*6)
        surface.blit(glow_surf, (x - radius*2, y - radius*2), special_flags=pygame.BLEND_RGBA_ADD)
    pygame.draw.circle(surface, color, pos, radius, 2)

def draw_arc(surface, color, center, radius, start_deg, end_deg, thickness=2):
    rect = pygame.Rect(center[0] - radius, center[1] - radius, radius*2, radius*2)
    pygame.draw.arc(surface, color, rect, math.radians(start_deg), math.radians(end_deg), thickness)

def draw_dashed_circle(surface, color, center, radius, dash_count=40, dash_len=5, thickness=2, rotation=0):
    for i in range(dash_count):
        angle1 = (360 / dash_count) * i + rotation
        angle2 = angle1 + dash_len
        draw_arc(surface, color, center, radius, angle1, angle2, thickness)

def draw_grid():
    spacing = 40
    for x in range(0, WIDTH, spacing):
        pygame.draw.line(screen, (10, 20, 35), (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, spacing):
        pygame.draw.line(screen, (10, 20, 35), (0, y), (WIDTH, y), 1)

def draw_corner_frame():
    c = (0, 180, 255)
    l = 45
    t = 3

    # top-left
    pygame.draw.line(screen, c, (20, 20), (20+l, 20), t)
    pygame.draw.line(screen, c, (20, 20), (20, 20+l), t)

    # top-right
    pygame.draw.line(screen, c, (WIDTH-20, 20), (WIDTH-20-l, 20), t)
    pygame.draw.line(screen, c, (WIDTH-20, 20), (WIDTH-20, 20+l), t)

    # bottom-left
    pygame.draw.line(screen, c, (20, HEIGHT-20), (20+l, HEIGHT-20), t)
    pygame.draw.line(screen, c, (20, HEIGHT-20), (20, HEIGHT-20-l), t)

    # bottom-right
    pygame.draw.line(screen, c, (WIDTH-20, HEIGHT-20), (WIDTH-20-l, HEIGHT-20), t)
    pygame.draw.line(screen, c, (WIDTH-20, HEIGHT-20), (WIDTH-20, HEIGHT-20-l), t)

# =========================
# PARTICLES
# =========================
particles = []
for _ in range(120):
    particles.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "speed": random.uniform(0.2, 1.0),
        "size": random.randint(1, 3)
    })

def update_particles():
    for p in particles:
        p["y"] += p["speed"]
        if p["y"] > HEIGHT:
            p["y"] = 0
            p["x"] = random.randint(0, WIDTH)

def draw_particles():
    for p in particles:
        pygame.draw.circle(screen, (40, 120, 180), (int(p["x"]), int(p["y"])), p["size"])

# =========================
# DATA BARS
# =========================
def draw_data_bars(x, y, count=8, width=220, height=14, seed=0):
    random.seed(seed)
    for i in range(count):
        bar_w = random.randint(50, width)
        pygame.draw.rect(screen, (15, 35, 55), (x, y + i*28, width, height), border_radius=4)
        pygame.draw.rect(screen, CYAN, (x, y + i*28, bar_w, height), border_radius=4)

# =========================
# LEFT PANEL
# =========================
def draw_left_panel(t):
    panel = pygame.Rect(35, 110, 340, 680)
    pygame.draw.rect(screen, (8, 18, 30), panel, border_radius=14)
    pygame.draw.rect(screen, (0, 160, 255), panel, 2, border_radius=14)

    draw_text("SYSTEM ANALYTICS", font_medium, CYAN, 60, 130)
    draw_text("NEURAL PROCESSING", font_small, SOFT_CYAN, 60, 175)
    draw_data_bars(60, 205, count=6, seed=int(t*10)%1000)

    draw_text("TARGET ACQUISITION", font_small, SOFT_CYAN, 60, 400)
    for i in range(5):
        y = 430 + i*42
        pygame.draw.rect(screen, (15, 30, 45), (60, y, 280, 28), border_radius=6)
        val = random.randint(35, 99)
        draw_text(f"ENTITY_{i+1:02d}", font_small, WHITE, 70, y+4)
        draw_text(f"{val}%", font_small, GREEN if val > 70 else YELLOW, 280, y+4)

    draw_text("SIGNAL STABILITY", font_small, SOFT_CYAN, 60, 650)
    stability = 82 + int(10 * math.sin(t * 2))
    pygame.draw.rect(screen, (15, 35, 55), (60, 680, 250, 18), border_radius=5)
    pygame.draw.rect(screen, GREEN, (60, 680, stability * 2.4, 18), border_radius=5)
    draw_text(f"{stability}%", font_small, WHITE, 320, 678)

# =========================
# RIGHT PANEL
# =========================
def draw_right_panel(t):
    panel = pygame.Rect(WIDTH - 375, 110, 340, 680)
    pygame.draw.rect(screen, (8, 18, 30), panel, border_radius=14)
    pygame.draw.rect(screen, (0, 160, 255), panel, 2, border_radius=14)

    draw_text("TACTICAL FEED", font_medium, CYAN, WIDTH - 350, 130)

    # Radar box
    radar_rect = pygame.Rect(WIDTH - 340, 180, 270, 220)
    pygame.draw.rect(screen, (10, 22, 35), radar_rect, border_radius=10)
    pygame.draw.rect(screen, CYAN, radar_rect, 2, border_radius=10)

    rx, ry = radar_rect.center
    rr = 80
    pygame.draw.circle(screen, (0, 120, 180), (rx, ry), rr, 1)
    pygame.draw.circle(screen, (0, 120, 180), (rx, ry), rr//2, 1)
    pygame.draw.line(screen, (0, 120, 180), (rx-rr, ry), (rx+rr, ry), 1)
    pygame.draw.line(screen, (0, 120, 180), (rx, ry-rr), (rx, ry+rr), 1)

    sweep_angle = (t * 120) % 360
    end_x = rx + rr * math.cos(math.radians(sweep_angle))
    end_y = ry + rr * math.sin(math.radians(sweep_angle))
    pygame.draw.line(screen, GREEN, (rx, ry), (end_x, end_y), 2)

    for i in range(6):
        angle = (t * 40 + i * 60) % 360
        px = rx + (rr - 20) * math.cos(math.radians(angle))
        py = ry + (rr - 20) * math.sin(math.radians(angle))
        pygame.draw.circle(screen, RED if i % 2 == 0 else YELLOW, (int(px), int(py)), 4)

    draw_text("MISSION PARAMETERS", font_small, SOFT_CYAN, WIDTH - 350, 440)
    for i in range(6):
        y = 470 + i*42
        pygame.draw.rect(screen, (15, 30, 45), (WIDTH - 350, y, 280, 28), border_radius=6)
        draw_text(f"PROTOCOL_{i+1:02d}", font_small, WHITE, WIDTH - 340, y+4)
        draw_text("ACTIVE", font_small, GREEN, WIDTH - 150, y+4)

# =========================
# TOP BAR
# =========================
def draw_top_bar(t):
    pygame.draw.rect(screen, (8, 18, 30), (0, 0, WIDTH, 70))
    pygame.draw.line(screen, CYAN, (0, 70), (WIDTH, 70), 2)

    draw_text("EDITH", font_xl, CYAN, 120, 35, center=True)
    draw_text("EVEN DEAD, I'M THE HERO", font_small, SOFT_CYAN, 220, 26)

    current_time = datetime.now().strftime("%H:%M:%S")
    draw_text(f"TIME: {current_time}", font_medium, WHITE, WIDTH - 280, 20)

    # top pulse dots
    for i in range(10):
        x = WIDTH//2 - 180 + i*40
        radius = 4 + int(2 * math.sin(t*4 + i))
        pygame.draw.circle(screen, CYAN, (x, 35), radius)

# =========================
# BOTTOM BAR
# =========================
def draw_bottom_bar(t):
    pygame.draw.rect(screen, (8, 18, 30), (0, HEIGHT-70, WIDTH, 70))
    pygame.draw.line(screen, CYAN, (0, HEIGHT-70), (WIDTH, HEIGHT-70), 2)

    commands = [
        "TARGET LOCK",
        "SCAN MODE",
        "TACTICAL VIEW",
        "DEFENSE GRID",
        "AI OVERRIDE",
        "DRONE LINK"
    ]

    x = 80
    for i, cmd in enumerate(commands):
        w = 180
        rect = pygame.Rect(x, HEIGHT-55, w, 36)
        pygame.draw.rect(screen, (10, 28, 45), rect, border_radius=8)
        pygame.draw.rect(screen, CYAN if i != 4 else RED, rect, 2, border_radius=8)
        draw_text(cmd, font_small, WHITE, x + 18, HEIGHT - 47)
        x += 210

# =========================
# CENTER HUD
# =========================
def draw_center_hud(t):
    cx, cy = WIDTH // 2, HEIGHT // 2 + 20

    # Outer rings
    draw_glow_circle(screen, SOFT_CYAN, (cx, cy), 220, 6)
    pygame.draw.circle(screen, (0, 120, 180), (cx, cy), 250, 1)
    pygame.draw.circle(screen, (0, 120, 180), (cx, cy), 280, 1)

    # Dashed rotating rings
    draw_dashed_circle(screen, CYAN, (cx, cy), 250, dash_count=48, dash_len=4, thickness=2, rotation=t*35)
    draw_dashed_circle(screen, BLUE, (cx, cy), 200, dash_count=36, dash_len=6, thickness=2, rotation=-t*55)
    draw_dashed_circle(screen, SOFT_CYAN, (cx, cy), 160, dash_count=28, dash_len=8, thickness=2, rotation=t*75)

    # Rotating arcs
    draw_arc(screen, GREEN, (cx, cy), 230, (t*90)%360, (t*90)%360 + 60, 4)
    draw_arc(screen, YELLOW, (cx, cy), 185, (-t*110)%360, (-t*110)%360 + 45, 4)
    draw_arc(screen, RED, (cx, cy), 145, (t*140)%360, (t*140)%360 + 30, 4)

    # Crosshair lines
    pygame.draw.line(screen, (0, 100, 180), (cx-320, cy), (cx+320, cy), 1)
    pygame.draw.line(screen, (0, 100, 180), (cx, cy-320), (cx, cy+320), 1)

    # Orbiting nodes
    for i in range(8):
        angle = t * 35 + i * 45
        r = 220
        x = cx + r * math.cos(math.radians(angle))
        y = cy + r * math.sin(math.radians(angle))
        draw_glow_circle(screen, CYAN, (int(x), int(y)), 5, 3)

    for i in range(6):
        angle = -t * 55 + i * 60
        r = 160
        x = cx + r * math.cos(math.radians(angle))
        y = cy + r * math.sin(math.radians(angle))
        pygame.draw.circle(screen, YELLOW, (int(x), int(y)), 4)

    # Core pulse
    pulse = 40 + int(8 * math.sin(t * 4))
    draw_glow_circle(screen, CYAN, (cx, cy), pulse, 8)
    pygame.draw.circle(screen, WHITE, (cx, cy), 10)

    # Inner hex-like nodes
    for i in range(6):
        angle = i * 60 + t * 25
        r = 85
        x = cx + r * math.cos(math.radians(angle))
        y = cy + r * math.sin(math.radians(angle))
        pygame.draw.line(screen, SOFT_CYAN, (cx, cy), (x, y), 1)
        pygame.draw.circle(screen, SOFT_CYAN, (int(x), int(y)), 6, 2)

    # Text labels
    draw_text("EDITH AI CORE", font_large, CYAN, cx, cy - 18, center=True)
    draw_text("TACTICAL INTELLIGENCE ACTIVE", font_small, WHITE, cx, cy + 28, center=True)

    # Dynamic percentage
    power = 92 + int(5 * math.sin(t * 2))
    draw_text(f"{power}%", font_xl, GREEN, cx, cy + 90, center=True)

# =========================
# SCAN LINES
# =========================
def draw_scan_line(t):
    y = int((t * 250) % HEIGHT)
    line_surf = pygame.Surface((WIDTH, 8), pygame.SRCALPHA)
    pygame.draw.rect(line_surf, (0, 255, 255, 30), (0, 0, WIDTH, 8))
    screen.blit(line_surf, (0, y))

# =========================
# MAIN LOOP
# =========================
def main():
    running = True
    start_ticks = pygame.time.get_ticks()

    while running:
        clock.tick(60)
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Background
        screen.fill(BG)
        draw_grid()
        update_particles()
        draw_particles()

        # UI Layers
        draw_corner_frame()
        draw_top_bar(t)
        draw_bottom_bar(t)
        draw_left_panel(t)
        draw_right_panel(t)
        draw_center_hud(t)
        draw_scan_line(t)

        # subtle vignette effect
        vignette = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(vignette, (0, 0, 0, 35), (0, 0, WIDTH, HEIGHT), border_radius=0)
        screen.blit(vignette, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def start_hud():
    """Entry point for HUD"""
    if 'IronHUD' in globals():
        hud = IronHUD()
        if hasattr(hud, 'run'):
            hud.run()
        else:
            raise AttributeError("IronHUD class exists but has no run() method")
    elif 'run_hud' in globals():
        run_hud()
    elif 'main' in globals():
        main()
    else:
        raise ImportError("No valid HUD entry point found in iron_hud.py")

if __name__ == "__main__":
    start_hud()