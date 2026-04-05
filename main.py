import pygame

from settings import *
from ball import Ball
from paddle import Paddle
from levels import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
running = True

paddle = Paddle()
ball = Ball()

bricks = create_level(LEVEL_1)

while running:
    # poll for events
    # pygame.QUIT events means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with black to wipe away anything from last frame
    screen.fill(get_theme()["background"])

    # Game logic goes here
    paddle.draw_paddle(screen)
    paddle.move()

    ball.draw_ball(screen)
    ball.move()
    ball.bounce(paddle)
    ball.reset(paddle)

    for brick in bricks[:]:
        brick.draw_brick(screen)
        if brick.hit(ball):
            bricks.remove(brick)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()