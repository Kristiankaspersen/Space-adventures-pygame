from random import randint, randrange

import pygame


class Asteroid:
    """Making the Asteroid """
    def __init__(self, window):
        self.window = window
        self.asteroid_img = pygame.image.load("img/asteroid.png").convert_alpha()
        self.asteroid_w = randint(150, 300)
        self.asteroid_h = randint(150, 300)
        self.poop_img = pygame.transform.scale(self.asteroid_img,
                                               (self.asteroid_w, self.asteroid_h))
        self.rect_x = randrange(50, 700, 10)
        self.rect_y = -50
        self.rect_y_vel = randint(5, 15)

    def draw(self):
        """Draws the asteroid on the screen """
        self.window.blit(self.asteroid_img, (self.rect_x, self.rect_y))

    def move(self):
        """Moves the asteroid on the screen downward"""
        self.rect_y += self.rect_y_vel

        if self.rect_y >= 820:
            self.rect_x = randrange(50, 700, 10)
            self.rect_y = -50