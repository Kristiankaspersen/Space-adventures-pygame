import math

import pygame

from util.enums import BulletStatus


# Ready - You can´t see the bullet on the screen
# Fire - The bullet is currently moving

class Bullet:
    """Makes the bullet"""
    def __init__(self, window):
        self.window = window
        self.bullet_img = pygame.image.load("img/bullet.png").convert_alpha()
        self.bullet_y = 800
        self.bullet_vel = 50
        self.bullet_status = BulletStatus.READY
        self.bullet_x = 0

    # Ready - You can´t see the bullet on the screen
    # Fire - The bullet is currently moving
    def fire_bullet(self, bullet_x):
        """The bullet will show when an applied button is pressed
        , and the spaceship will appear where the spaceship is positioned

            :param: takes inn the x-axis position of the spaceship
        """
        self.adjust_y = 75
        self.adjust_x = 4
        self.bullet_status = BulletStatus.FIRE
        self.window.blit(self.bullet_img, (bullet_x + self.adjust_x, self.bullet_y - self.adjust_y))

    def bullet_move(self):
        """Moves the bullet upward on the window screen"""
        self.bullet_y -= self.bullet_vel

        if self.bullet_y <= 0:
            self.bullet_y = 800
            self.bullet_status = BulletStatus.READY


# The collision function
def bullet_collision(poop_x, poop_y, bullet_x, bullet_y):
    # Putting a mathematical formel for distance
    distance = math.sqrt((math.pow(poop_x - bullet_x, 2)) + (math.pow(poop_y - bullet_y, 2)))

    if distance < 40:
        return True
    else:
        return False