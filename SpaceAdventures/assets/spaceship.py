import pygame


class Spaceship:
    """Making the spaceship Class
    :param: Taking inn window parameter for the possibility to display on screen
    """
    def __init__(self, window):
        self.window = window
        self.spaceship_img = pygame.image.load("img/battleship.png").convert_alpha()
        self.spaceship_w = 40
        self.spaceship_h = 60
        self.spaceship_img = pygame.transform.scale(self.spaceship_img,
                                                    (self.spaceship_w, self.spaceship_h))
        self.rect_x = 100
        self.rect_y = 800 - self.spaceship_h
        self.spaceship_vel = 15

    def border(self):
        """Border for each end of x-axis so the spaceship stay inside """
        if self.rect_x <= 0:
            self.rect_x = 0
        elif self.rect_x >= 750:
            self.rect_x = 750

    def draw(self):
        """Draws the spaceship to the window screen"""
        self.window.blit(self.spaceship_img, (self.rect_x, self.rect_y))

    def move_left(self):
        """Moves the spaceship to the left"""
        self.rect_x -= self.spaceship_vel

    def move_right(self):
        """Moves the spaceship to the right"""
        self.rect_x += self.spaceship_vel