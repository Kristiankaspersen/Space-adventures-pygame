import json

import pygame

from assets.asteroid import Asteroid
from assets.bullet import Bullet
from assets.score import ScoreDisplay
from assets.spacepoop import Spacepoop
from assets.spaceship import Spaceship


def game_setup():

    window_w = 800
    window_h = 900

    window = pygame.display.set_mode((window_w, window_h))
    pygame.display.set_caption("Spacepoop adventures")

    return window


def game_over_text(window, score):
    over_font = pygame.font.Font("freesansbold.ttf", 50)
    score_font = pygame.font.Font("freesansbold.ttf", 50)
    over_text = over_font.render(f"GAME OVER", True, (255, 255, 255))
    score_text = score_font.render(f"Your score: {score.score_sum}", True, (255, 255, 255))
    high_score_text = score_font.render(f"High score: {score.read_high_score()}", True, (255, 255, 255))
    window.blit(score_text, (200, 200))
    window.blit(high_score_text, (200, 300))
    window.blit(over_text, (200, 400))



