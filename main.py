import pygame

from gamemanager import GameManager
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
game_manager = GameManager()

bricks = create_level(LEVELS[game_manager.level - 1])

while running:
    # Poll for events
    # pygame.QUIT events means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.launched = True

    # Fill the screen with black to wipe away anything from the last frame
    screen.fill(get_theme()["background"])
    # Draw the HUD
    game_manager.draw_hud(screen)

    # Game logic goes here
    paddle.draw_paddle(screen)
    paddle.move()

    ball.draw_ball(screen)
    ball.move(paddle)
    ball.bounce(paddle, bricks)

    # Draw bricks and check for collisions
    ball_bounced = False                    # Ensure only one bounce per frame
    for brick in bricks[:]:
        brick.draw_brick(screen)
        if brick.hit(ball):
            # Handle side and top/bottom collisions
            if not ball_bounced:
                overlap_left = (ball.x_pos + ball.radius) - brick.x_pos
                overlap_right = (brick.x_pos + brick.width) - (ball.x_pos - ball.radius)
                overlap_top = (ball.y_pos + ball.radius) - brick.y_pos
                overlap_bottom = (brick.y_pos + brick.height) - (ball.y_pos - ball.radius)

                if ball.y_vel < 0:                          # moving up — can only hit bottom
                    overlap_top = float('inf')                  # impossible -> ignore it
                if ball.y_vel > 0:                          # moving down — can only hit top
                    overlap_bottom = float('inf')               # impossible -> ignore it
                if ball.x_vel < 0:                          # moving left — can only hit right side
                    overlap_left = float('inf')                 # impossible -> ignore it
                if ball.x_vel > 0:                          # moving right — can only hit left side
                    overlap_right = float('inf')                # impossible -> ignore it

                # Determine which side got hit first
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                # If side hit, reverse x velocity
                if min_overlap == overlap_left or min_overlap == overlap_right:
                    ball.x_vel *= -1  # side hit
                # If top/bottom hit, reverse y velocity
                else:
                    ball.y_vel *= -1  # top/bottom hit
                ball_bounced = True         # Ensure only one bounce per frame
            # Check if the brick is dead
            if brick.is_dead():
                bricks.remove(brick)
                game_manager.update_score(brick.max_hp)

    # Check if all bricks are dead
    if len(bricks) == 0:
        # Check if the level is complete
        if game_manager.level < len(LEVELS):
            game_manager.next_level()
            bricks = create_level(LEVELS[game_manager.level - 1])
            ball.launched = False
        # Check if the game is complete
        else:
            break

    # Check if the ball has reached the bottom of the screen
    if ball.y_pos > WINDOW_SIZE[1] - ball.radius:
        game_manager.lose_life()
        ball.reset(paddle)

    # Check if game is over
    if game_manager.lives <= 0:
        paddle.reset()
        ball.reset(paddle)
        game_manager.game_over()
        break

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()