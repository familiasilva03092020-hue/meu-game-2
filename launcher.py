# -*- coding: utf-8 -*-
import pygame
import sys
import subprocess
import os
import math

pygame.init()

WIDTH, HEIGHT = 640, 480
FPS = 60
TITLE = "Aventura Espacial - Launcher"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUNDS_DIR = os.path.join(BASE_DIR, "sounds")
GAME_FILE = os.path.join(BASE_DIR, "index.py")

BLACK = (10, 10, 20)
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
YELLOW = (255, 200, 50)
GRAY = (80, 80, 80)

pygame.font.init()
title_font = pygame.font.Font(None, 72)
menu_font = pygame.font.Font(None, 36)

music_path = os.path.join(SOUNDS_DIR, "musica_fundo_8bit.mp3")
if os.path.exists(music_path):
    try:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("Erro ao carregar música:", e)
else:
    print("Música de fundo não encontrada:", music_path)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

buttons = [
    {"text": "JOGAR", "rect": pygame.Rect(WIDTH//2 - 120, 220, 240, 56), "color": BLUE},
    {"text": "CONFIGURAÇÕES", "rect": pygame.Rect(WIDTH//2 - 120, 296, 240, 50), "color": GRAY},
    {"text": "SAIR", "rect": pygame.Rect(WIDTH//2 - 120, 360, 240, 50), "color": (200, 60, 60)}
]

HOVER_OFFSET = 25

def draw_menu(mouse_pos=None):
    screen.fill(BLACK)
    t = pygame.time.get_ticks() / 500.0
    pulse = 8 + int((1 + math.sin(t)) * 4)
    title = title_font.render("Aventura Espacial", True, YELLOW)
    title_rect = title.get_rect(center=(WIDTH//2, 100 - pulse//8))
    screen.blit(title, title_rect)

    for btn in buttons:
        rect = btn["rect"]
        color = btn["color"]
        if mouse_pos and rect.collidepoint(mouse_pos):
            color = tuple(min(255, c + HOVER_OFFSET) for c in color)
        pygame.draw.rect(screen, color, rect, border_radius=12)
        text = menu_font.render(btn["text"], True, WHITE)
        screen.blit(text, text.get_rect(center=rect.center))
    pygame.display.flip()

def main():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                for btn in buttons:
                    if btn["rect"].collidepoint(pos):
                        if btn["text"] == "JOGAR":
                            try:
                                pygame.mixer.music.stop()
                            except:
                                pass
                            try:
                                subprocess.Popen(["pgzrun", GAME_FILE])
                            except Exception:
                                subprocess.Popen([sys.executable, GAME_FILE])
                            pygame.quit()
                            sys.exit()
                        elif btn["text"] == "CONFIGURAÇÕES":
                            print("Tela de configurações em desenvolvimento...")
                        elif btn["text"] == "SAIR":
                            pygame.quit()
                            sys.exit()
        draw_menu(mouse_pos)
        clock.tick(FPS)

if __name__ == "__main__":
    main()
