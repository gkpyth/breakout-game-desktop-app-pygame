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
    ball.bounce(paddle, bricks)
    ball.reset(paddle)

    ball_bounced = False
    for brick in bricks[:]:
        brick.draw_brick(screen)
        if brick.hit(ball):
            if not ball_bounced:
                overlap_left = (ball.x_pos + ball.radius) - brick.x_pos
                overlap_right = (brick.x_pos + brick.width) - (ball.x_pos - ball.radius)
                overlap_top = (ball.y_pos + ball.radius) - brick.y_pos
                overlap_bottom = (brick.y_pos + brick.height) - (ball.y_pos - ball.radius)

                if ball.y_vel < 0:                          # moving up — can only hit bottom
                    overlap_top = float('inf')              # impossible, ignore it
                if ball.y_vel > 0:                          # moving down — can only hit top
                    overlap_bottom = float('inf')
                if ball.x_vel < 0:                          # moving left — can only hit right side
                    overlap_left = float('inf')
                if ball.x_vel > 0:                          # moving right — can only hit left side
                    overlap_right = float('inf')

                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                if min_overlap == overlap_left or min_overlap == overlap_right:
                    ball.x_vel *= -1  # side hit
                else:
                    ball.y_vel *= -1  # top/bottom hit
                ball_bounced = True
            if brick.is_dead():
                bricks.remove(brick)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()