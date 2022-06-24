from random import randrange

from assets.bullet import bullet_collision
from util.constants import BLACK
from util.enums import BulletStatus


def running_game(running, window, pygame, spaceship, bullet, poop, asteroid, score):
    pygame.display.set_caption("IN THE GAME")
    while running:
        pygame.time.delay(30)
        for event in pygame.event.get():  # Looping though a list of keyboard and mouse events
            if event.type == pygame.QUIT:
                return False

        window.fill(BLACK)

        # Draws the characters
        spaceship.draw()
        poop.draw()
        asteroid.draw()
        asteroid.move()
        spaceship.border()
        poop.move()  # makes the poop move on screen, and stay inside the screen border

        keys = pygame.key.get_pressed()  # Gives a dict with a value of 1 when pressed and 0 when not.

        # keyboard key a or left arrow wil move the spaceship to the right
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            spaceship.move_left()

        # keyboard key d or right arrow wil move the spaceship to the right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            spaceship.move_right()

        # The bullet will show on screen when you press enter or space
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if bullet.bullet_status == BulletStatus.READY:
                bullet.bullet_x = spaceship.rect_x
                bullet.fire_bullet(bullet.bullet_x)

        # When the bullet is fired, the bullet will move upward

        if bullet.bullet_status == BulletStatus.FIRE:
            bullet.fire_bullet(bullet.bullet_x)
            bullet.bullet_move()

        # Collision
        collision = bullet_collision(poop.rect_x, poop.rect_y, bullet.bullet_x, bullet.bullet_y)
        if collision:
            bullet.bullet_y = 800
            bullet.bullet_status = BulletStatus.READY
            score.score_sum += 10
            poop.rect_x = randrange(50, 700, 10)
            poop.rect_y = randrange(0, 150, 20)

            # Draw scoreboard
        score.display_score()

        # Game Over:
        if poop.rect_y > 800:
            return True

        pygame.display.update()