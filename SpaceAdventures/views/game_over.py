
from setup import game_over_text
from util.constants import BLACK

from assets.button import Button


def game_over(running, pygame, window, spaceship, poop, asteroid, score):

    exit_img = pygame.image.load("img/exit.png").convert_alpha()
    repeat_img = pygame.image.load("img/repeat.png").convert_alpha()
    exit_button = Button(500, 600, exit_img, 1)

    repeat_btn = Button(200, 600, repeat_img, 1)

    pygame.display.set_caption("Game over")
    while running:
        for event in pygame.event.get():  # Looping though a list of keyboard and mouse events
            if event.type == pygame.QUIT:
                return False

        window.fill(BLACK)

        spaceship.draw()
        poop.draw()
        asteroid.draw()

        game_over_text(window, score)
        if exit_button.draw(window):
            return False

        if repeat_btn.draw(window):
            poop.rect_y = 0
            return True

        pygame.display.update()