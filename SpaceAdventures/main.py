from random import randrange

import pygame
import json
from assets.spaceship import Spaceship
from assets.asteroid import Asteroid
from assets.score import ScoreDisplay
from util.constants import PASTEL_BLUE, BLACK
from assets.bullet import Bullet, bullet_collision
from assets.spacepoop import Spacepoop
from assets.button import Button
from views.game import running_game

from setup import game_setup, game_over_text
from util.enums import BulletStatus
from views.game_over import game_over

pygame.init()

window = game_setup()

start_img = pygame.image.load("img/start.png").convert_alpha()
exit_img = pygame.image.load("img/exit.png").convert_alpha()

# The characters in the game:
spaceship = Spaceship(window)
bullet = Bullet(window)
poop = Spacepoop(window)
asteroid = Asteroid(window)
score = ScoreDisplay(window)

start_button = Button(200, 100, start_img, 1)
exit_button = Button(200, 200, exit_img, 1)

running = True
while running:
    pygame.time.delay(30)  # delaying the game 0.3 seconds and slows it down
    for event in pygame.event.get():  # Looping though a list of keyboard and mouse events
        if event.type == pygame.QUIT:
            running = False

    while running:

        window.fill(PASTEL_BLUE)

        for event in pygame.event.get():  # Looping though a list of keyboard and mouse events
            if event.type == pygame.QUIT:
                running = False

        if start_button.draw(window):
            running = running_game(running, window, pygame, spaceship, bullet, poop, asteroid, score)
            running = game_over(running, pygame, window, spaceship, poop, asteroid, score)
        if exit_button.draw(window):
            running = False


        pygame.display.update()

    pygame.display.update()

pygame.quit()

score.write_new_high_score()



