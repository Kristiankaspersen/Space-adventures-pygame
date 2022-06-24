from random import randrange, randint

import pygame


class Spacepoop:
    def __init__(self, window):
        self.window = window
        self.poop_img = pygame.image.load("img/poop.png").convert_alpha()
        self.poop_w = 40
        self.poop_h = 60
        self.poop_img = pygame.transform.scale(self.poop_img,
                                               (self.poop_w, self.poop_h))
        self.rect_x = randrange(0, 800, 10)
        self.rect_y = randrange(0, 300, 20)
        self.poop_x_vel = 10
        self.poop_y_vel = randint(3, 8)

    def draw(self):
        """Draws the spaceship to the window screen"""
        self.window.blit(self.poop_img, (self.rect_x, self.rect_y))

    def move(self):
        """Moves the poop on the screen, in the x-axis and y-axis"""
        self.rect_x += self.poop_x_vel
        self.rect_y += self.poop_y_vel

        # When the poop hits the border it will turn and move the other way
        if self.rect_x <= 5:
            self.poop_x_vel += 3
        elif self.rect_x >= 736:
            self.poop_x_vel -= 10