# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pgzrun
import pygame
import random
from pgzero.actor import Actor as PGZActor, Actor

WIDTH = 600
HEIGHT = 450
TITLE = "Aventura Espacial"
FPS = 30

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
SOUNDS_DIR = os.path.join(BASE_DIR, "sounds")

ship_image_path = os.path.join(IMAGES_DIR, "ship.png")
if os.path.exists(ship_image_path):
    ship_surface = pygame.image.load(ship_image_path).convert_alpha()
    class CustomActor(PGZActor):
        def __init__(self, surface, pos):
            super().__init__("ship", pos)
            self._surf = surface
    ship = CustomActor(ship_surface, (300, 400))
else:
    ship = Actor("ship", (300, 400))

enemies = []
meteors = []
bullets = []
mode = 'menu'
difficulty = 'medio'
difficulty_speeds = {'facil': (2, 5), 'medio': (4, 8), 'dificil': (7, 12)}

button_play = Rect((WIDTH//2 - 60, HEIGHT//2 - 60), (120, 50))
button_facil = Rect((WIDTH//2 - 180, HEIGHT//2 + 20), (100, 40))
button_medio = Rect((WIDTH//2 - 50, HEIGHT//2 + 20), (100, 40))
button_dificil = Rect((WIDTH//2 + 80, HEIGHT//2 + 20), (100, 40))

def load_sound_safe(name, volume=0.6):
    path = os.path.join(SOUNDS_DIR, name)
    if os.path.exists(path):
        try:
            s = pygame.mixer.Sound(path)
            s.set_volume(volume)
            return s
        except Exception as e:
            print("Erro ao carregar som:", e)
    else:
        print("Som nao encontrado:", path)
    return None

shoot_sound = load_sound_safe("tiro.wav", 0.6)
gameover_sound = load_sound_safe("gameover.wav", 0.8)

music_path = os.path.join(SOUNDS_DIR, "musica_fundo_8bit.mp3")
if os.path.exists(music_path):
    try:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.4)
    except Exception as e:
        print("Erro ao carregar musica:", e)
else:
    print("Musica nao encontrada:", music_path)

def start_music():
    try:
        if os.path.exists(music_path) and not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
    except:
        pass

def stop_music():
    try:
        pygame.mixer.music.stop()
    except:
        pass

def start_game():
    global mode, enemies, meteors, bullets
    enemies.clear()
    meteors.clear()
    bullets.clear()

    min_speed, max_speed = difficulty_speeds[difficulty]

    for _ in range(5):
        x, y = random.randint(0, WIDTH), random.randint(-HEIGHT, -50)
        e = Actor("enemy", (x, y))
        e.speed = random.randint(min_speed, max_speed)
        enemies.append(e)

    for _ in range(5):
        x, y = random.randint(0, WIDTH), random.randint(-HEIGHT, -50)
        m = Actor("meteor", (x, y))
        m.speed = random.randint(min_speed, max_speed + 2)
        meteors.append(m)

    start_music()
    mode = 'game'

def draw():
    screen.clear()
    if mode == 'menu':
        screen.fill("black")
        screen.draw.text("AVENTURA ESPACIAL", center=(WIDTH//2, HEIGHT//2 - 120), fontsize=50, color="white")
        screen.draw.text("Criado por TOTOI", center=(WIDTH//2, HEIGHT - 30), fontsize=25, color="gray")

        screen.draw.filled_rect(button_play, "dodgerblue")
        screen.draw.text("JOGAR", center=button_play.center, fontsize=35, color="white")

        cor_facil = "green" if difficulty == "facil" else "gray"
        cor_medio = "yellow" if difficulty == "medio" else "gray"
        cor_dificil = "red" if difficulty == "dificil" else "gray"

        for rect, texto, cor in [
            (button_facil, "FACIL", cor_facil),
            (button_medio, "MEDIO", cor_medio),
            (button_dificil, "DIFICIL", cor_dificil)
        ]:
            screen.draw.filled_rect(rect, cor)
            screen.draw.text(texto, center=rect.center, fontsize=30, color="black")

    elif mode == 'game':
        screen.blit("space", (0, 0))
        for m in meteors: m.draw()
        for b in bullets: b.draw()
        ship.draw()
        for e in enemies: e.draw()

    elif mode == 'end':
        screen.blit("space", (0, 0))
        screen.draw.text("VOCE PERDEU", center=(WIDTH//2, HEIGHT//2), color="yellow", fontsize=36)
        screen.draw.text("CLIQUE PARA VOLTAR AO MENU", center=(WIDTH//2, HEIGHT//2 + 50), color="white", fontsize=24)

def on_mouse_move(pos):
    if mode == 'game':
        ship.pos = pos

def on_mouse_down(button, pos):
    global mode, difficulty
    if mode == 'menu':
        if button_play.collidepoint(pos): start_game()
        elif button_facil.collidepoint(pos): difficulty = "facil"
        elif button_medio.collidepoint(pos): difficulty = "medio"
        elif button_dificil.collidepoint(pos): difficulty = "dificil"
    elif mode == 'game' and button == 1:
        shoot()
    elif mode == 'end':
        mode = 'menu'
        start_music()

def shoot():
    b = Actor("bullet", (ship.x, ship.y - 40))
    b.speed = 10
    bullets.append(b)
    if shoot_sound:
        try: shoot_sound.play()
        except: pass

def update_bullets():
    for b in bullets[:]:
        b.y -= b.speed
        if b.y < 0:
            bullets.remove(b)

def new_enemy():
    min_speed, max_speed = difficulty_speeds[difficulty]
    x, y = random.randint(0, WIDTH), -50
    e = Actor("enemy", (x, y))
    e.speed = random.randint(min_speed, max_speed)
    enemies.append(e)

def enemy_ship():
    for e in enemies[:]:
        e.y += e.speed
        if e.y > HEIGHT + 100:
            enemies.remove(e)
            new_enemy()

def meteorites():
    min_speed, max_speed = difficulty_speeds[difficulty]
    for m in meteors:
        m.y += m.speed
        if m.y > HEIGHT:
            m.x = random.randint(0, WIDTH)
            m.y = -20
            m.speed = random.randint(min_speed, max_speed + 2)

def collisions():
    global mode
    bullets_to_remove = set()
    enemies_to_remove = set()
    meteors_to_remove = set()

    for e in enemies:
        if ship.colliderect(e):
            if gameover_sound:
                try: gameover_sound.play()
                except: pass
            stop_music()
            mode = 'end'
            return

    for m in meteors:
        if ship.colliderect(m):
            if gameover_sound:
                try: gameover_sound.play()
                except: pass
            stop_music()
            mode = 'end'
            return

    for b in bullets:
        for e in enemies:
            if b.colliderect(e):
                bullets_to_remove.add(b)
                enemies_to_remove.add(e)
                break
        for m in meteors:
            if b.colliderect(m):
                bullets_to_remove.add(b)
                meteors_to_remove.add(m)
                break

    for b in bullets_to_remove:
        if b in bullets: bullets.remove(b)
    for e in enemies_to_remove:
        if e in enemies:
            enemies.remove(e)
            new_enemy()
    for m in meteors_to_remove:
        if m in meteors: meteors.remove(m)

def update(dt):
    if mode == 'game':
        enemy_ship()
        meteorites()
        update_bullets()
        collisions()

pgzrun.go()
