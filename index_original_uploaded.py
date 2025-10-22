# -*- coding: utf-8 -*-

import pgzrun
import pygame
import random
from pgzero.actor import Actor as PGZActor

WIDTH = 600
HEIGHT = 450
TITLE = "Aventura espacial"
FPS = 30

# Caminho absoluto da imagem da nave (ajuste conforme seu ambiente)
ship_image_path = r"C:\Users\famil\Downloads\my game\images\ship.png"
ship_surface = pygame.image.load(ship_image_path).convert_alpha()

class CustomActor(PGZActor):
    def __init__(self, surface, pos):
        super().__init__("ship", pos)
        self._surf = surface

ship = CustomActor(ship_surface, (300, 400))

enemies = []
meteors = []
bullets = []

mode = 'menu'  # Comeca no menu

difficulty = 'medio'  # Padrao
difficulty_speeds = {
    'facil': (2, 5),   # inimigos e meteoros velocidade minima e maxima
    'medio': (4, 8),
    'dificil': (7, 12)
}

# Botoes para o menu (retangulos)
button_play = Rect((WIDTH//2 - 60, HEIGHT//2 - 60), (120, 50))
button_facil = Rect((WIDTH//2 - 180, HEIGHT//2 + 20), (100, 40))
button_medio = Rect((WIDTH//2 - 50, HEIGHT//2 + 20), (100, 40))
button_dificil = Rect((WIDTH//2 + 80, HEIGHT//2 + 20), (100, 40))

def start_game():
    global mode, enemies, meteors, bullets
    enemies.clear()
    meteors.clear()
    bullets.clear()

    min_speed, max_speed = difficulty_speeds[difficulty]

    # Inicializa inimigos
    for i in range(5):
        x = random.randint(0, WIDTH)
        y = random.randint(-HEIGHT, -50)
        enemy = Actor("enemy", (x, y))
        enemy.speed = random.randint(min_speed, max_speed)
        enemies.append(enemy)

    # Inicializa meteoros
    for i in range(5):
        x = random.randint(0, WIDTH)
        y = random.randint(-HEIGHT, -50)
        meteor = Actor("meteor", (x, y))
        meteor.speed = random.randint(min_speed, max_speed + 2)
        meteors.append(meteor)

    mode = 'game'

def draw():
    screen.clear()

    if mode == 'menu':
        screen.fill("black")
        screen.draw.text("AVENTURA ESPACIAL", center=(WIDTH//2, HEIGHT//2 - 120), fontsize=50, color="white")

        # Botao Jogar
        screen.draw.filled_rect(button_play, "dodgerblue")
        screen.draw.text("JOGAR", center=button_play.center, fontsize=35, color="white")

        # Botoes dificuldade
        cor_facil = "green" if difficulty == "facil" else "gray"
        cor_medio = "yellow" if difficulty == "medio" else "gray"
        cor_dificil = "red" if difficulty == "dificil" else "gray"

        screen.draw.filled_rect(button_facil, cor_facil)
        screen.draw.text("FACIL", center=button_facil.center, fontsize=30, color="black")

        screen.draw.filled_rect(button_medio, cor_medio)
        screen.draw.text("MEDIO", center=button_medio.center, fontsize=30, color="black")

        screen.draw.filled_rect(button_dificil, cor_dificil)
        screen.draw.text("DIFICIL", center=button_dificil.center, fontsize=30, color="black")

    elif mode == 'game':
        screen.blit("space", (0, 0))

        for meteor in meteors:
            meteor.draw()

        for bullet in bullets:
            bullet.draw()

        ship.draw()

        for enemy in enemies:
            enemy.draw()

    elif mode == 'end':
        screen.blit("space", (0, 0))
        screen.draw.text("VOCE PERDEU SEU RUIM KKKKK", center=(WIDTH//2, HEIGHT//2), color="yellow", fontsize=36)
        screen.draw.text("CLIQUE PARA VOLTAR AO MENU", center=(WIDTH//2, HEIGHT//2 + 50), color="white", fontsize=24)

def on_mouse_move(pos):
    if mode == 'game':
        ship.pos = pos

def on_mouse_down(button, pos):
    global mode, difficulty

    if mode == 'menu':
        if button_play.collidepoint(pos):
            start_game()

        elif button_facil.collidepoint(pos):
            difficulty = "facil"
        elif button_medio.collidepoint(pos):
            difficulty = "medio"
        elif button_dificil.collidepoint(pos):
            difficulty = "dificil"

    elif mode == 'game':
        if button == 1:  # Botao esquerdo
            shoot()

    elif mode == 'end':
        mode = 'menu'

def shoot():
    bullet = Actor("bullet", (ship.x, ship.y - 40))
    bullet._surf = pygame.transform.scale(bullet._surf, (bullet.width // 2, bullet.height // 2))
    bullet.width = bullet._surf.get_width()
    bullet.height = bullet._surf.get_height()
    bullet.speed = 10
    bullets.append(bullet)

    # 🔊 Som do tiro
    try:
        sounds.tiro.wav()
    except Exception as e:
        print("Erro ao tocar som do tiro:", e)

def update_bullets():
    for bullet in bullets[:]:
        bullet.y -= bullet.speed
        if bullet.y < 0:
            bullets.remove(bullet)

def new_enemy():
    min_speed, max_speed = difficulty_speeds[difficulty]
    x = random.randint(0, WIDTH)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(min_speed, max_speed)
    enemies.append(enemy)

def enemy_ship():
    for i in range(len(enemies) -1, -1, -1):
        if enemies[i].y < HEIGHT + 200:
            enemies[i].y += enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

def meteorites():
    min_speed, max_speed = difficulty_speeds[difficulty]
    for i in range(len(meteors)):
        if meteors[i].y < HEIGHT:
            meteors[i].y += meteors[i].speed
        else:
            meteors[i].x = random.randint(0, WIDTH)
            meteors[i].y = -20
            meteors[i].speed = random.randint(min_speed, max_speed + 2)

def collisions():
    global mode

    for enemy in enemies:
        if ship.colliderect(enemy):
            mode = 'end'

    for meteor in meteors:
        if ship.colliderect(meteor):
            mode = 'end'

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                new_enemy()
                break

    for bullet in bullets[:]:
        for meteor in meteors[:]:
            if bullet.colliderect(meteor):
                bullets.remove(bullet)
                meteors.remove(meteor)
                break

def update(dt):
    if mode == 'game':
        enemy_ship()
        meteorites()
        update_bullets()
        collisions()

pgzrun.go()
