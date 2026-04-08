import pygame
import random

from leaderboard import *
from ui import *
from gamemanager import GameManager
from powerup import PowerUp
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
game_manager = GameManager()

bricks = create_level(LEVELS[game_manager.level - 1])
balls = [Ball()]
powerups = []

initials = []

leaderboard_data = load_leaderboard()            # Load the leaderboard data: return data["leaderboard"]

while running:
    # Poll for events
    # pygame.QUIT events means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Start Screen
            if event.key == pygame.K_SPACE and game_manager.state == "start":
                game_manager.state = "playing"

            # Playing Screen
            elif event.key == pygame.K_SPACE and game_manager.state == "playing":
                for b in balls:
                    b.launched = True

            # Game Over Screen: Initials Entry
            elif game_manager.state == "game_over" and not game_manager.score_saved:
                if pygame.K_a <= event.key <= pygame.K_z and len(initials) < 3:
                    letter = chr(event.key).upper()
                    initials.append(letter)
                    if len(initials) == 3:
                        save_score("".join(initials), game_manager.score)
                        game_manager.score_saved = True
                        game_manager.score_saved_time = pygame.time.get_ticks()
                elif event.key == pygame.K_BACKSPACE and len(initials) > 0:
                    initials.pop()

            # Game Over Screen: Restart
            elif event.key == pygame.K_SPACE and game_manager.state == "game_over" and game_manager.score_saved:
                    bricks, balls, powerups, initials, leaderboard_data = game_manager.reset_game(paddle)
                    game_manager.state = "playing"

            # Victory Screen: Initials Entry
            elif game_manager.state == "victory" and not game_manager.score_saved:
                if pygame.K_a <= event.key <= pygame.K_z and len(initials) < 3:
                    letter = chr(event.key).upper()
                    initials.append(letter)
                    if len(initials) == 3:
                        save_score("".join(initials), game_manager.score)
                        game_manager.score_saved = True
                        game_manager.score_saved_time = pygame.time.get_ticks()
                elif event.key == pygame.K_BACKSPACE and len(initials) > 0:
                    initials.pop()

            # Victory Screen: Restart
            elif event.key == pygame.K_SPACE and game_manager.state == "victory":
                bricks, balls, powerups, initials, leaderboard_data = game_manager.reset_game(paddle)
                game_manager.state = "playing"

            # Pause Screen
            if event.key == pygame.K_ESCAPE and game_manager.state == "playing":
                game_manager.state = "paused"
            elif event.key == pygame.K_ESCAPE and game_manager.state == "paused":
                game_manager.state = "playing"

    if game_manager.state == "start":
        # Draw the start screen - await for Space
        draw_start_screen(screen, leaderboard_data)

    elif game_manager.state == "playing":
        # Fill the screen with black to wipe away anything from the last frame
        screen.fill(get_theme()["background"])
        # Draw the HUD
        game_manager.draw_hud(screen)

        # Game logic goes here
        paddle.draw_paddle(screen)
        paddle.move()
        paddle.check_powerup()

        for ball in balls[:]:
            ball.draw_ball(screen)
            ball.move(paddle)
            ball.bounce(paddle, bricks)
            ball.check_powerup()

        # Draw bricks
        for brick in bricks[:]:
            brick.draw_brick(screen)

        # Check ball-brick collisions
        for ball in balls[:]:
            ball_bounced = False                    # Ensure only one bounce per ball per frame
            for brick in bricks[:]:
                if brick.hit(ball):
                    if not ball_bounced:
                        # Check which face the ball is approaching based on velocity + position.
                        # Since ball speed (5px) < ball radius (10px), the center is always
                        # still outside the brick's face on first contact — making these reliable.
                        hit_side = (
                            (ball.x_vel < 0 and ball.x_pos > brick.x_pos + brick.width) or  # approaching right face
                            (ball.x_vel > 0 and ball.x_pos < brick.x_pos)                    # approaching left face
                        )
                        hit_top_bottom = (
                            (ball.y_vel < 0 and ball.y_pos > brick.y_pos + brick.height) or  # approaching bottom face
                            (ball.y_vel > 0 and ball.y_pos < brick.y_pos)                    # approaching top face
                        )

                        if hit_side and not hit_top_bottom:
                            ball.x_vel *= -1
                        elif hit_top_bottom and not hit_side:
                            ball.y_vel *= -1
                        else:
                            # Corner: both faces or neither (deep penetration) — use velocity magnitude
                            if abs(ball.y_vel) >= abs(ball.x_vel):
                                ball.y_vel *= -1
                            else:
                                ball.x_vel *= -1
                        ball_bounced = True

                    # Check if the brick is dead
                    if brick.is_dead():
                        bricks.remove(brick)
                        game_manager.update_score(brick.max_hp)
                        if random.random() < powerup_drop_chance:
                            powerups.append(PowerUp(brick.x_pos, brick.y_pos))

        for powerup in powerups[:]:
            powerup.draw_powerup(screen)
            powerup.drop_powerup()
            if powerup.paddle_collision(paddle):
                if powerup.type == "wide":
                    paddle.activate_wide_powerup(powerup.type)
                elif powerup.type == "slow":
                    for ball in balls[:]:
                        ball.activate_slow_powerup(powerup.type)
                elif powerup.type == "multi":
                    # Spawn 2 new balls at the current ball's position, mirroring its velocity
                    reference_ball = next((ball for ball in balls if ball.launched), None)
                    if reference_ball:
                        for x_flip, y_flip in [(-1, 1), (1, -1)]:
                            new_ball = Ball()
                            new_ball.launched = True
                            new_ball.x_pos = reference_ball.x_pos
                            new_ball.y_pos = reference_ball.y_pos
                            new_ball.x_vel = reference_ball.x_vel * x_flip
                            new_ball.y_vel = reference_ball.y_vel * y_flip
                            balls.append(new_ball)
                    else:
                        balls.append(Ball())
                        balls.append(Ball())
                elif powerup.type == "life":
                    game_manager.activate_life_powerup(powerup.type)
                powerups.remove(powerup)

        if not balls[0].launched:
            draw_pulsing_ball_release_text(screen)

        # Check if all bricks are dead
        if len(bricks) == 0:
            # Check if the level is complete
            if game_manager.level < len(LEVELS):
                game_manager.next_level()
                bricks = create_level(LEVELS[game_manager.level - 1])
                balls = [Ball()]
                powerups = []
                paddle.reset_powerup()
            # Check if the game is complete
            else:
                game_manager.state = "victory"

        # Check if a ball has reached the bottom of the screen and remove it from the list
        for ball in balls[:]:
            if ball.y_pos > WINDOW_SIZE[1] - ball.radius:
                balls.remove(ball)

        # Deduct a life if the last ball has reached the bottom of the screen
        if len(balls) <= 0:
            game_manager.lose_life()
            balls = [Ball()]
            balls[0].reset(paddle)

        # Check if game is over
        if game_manager.lives <= 0:
            game_manager.state = "game_over"

    elif game_manager.state == "paused":
        # Draw the pause overlay, wait for unpause
        # Draw the game frozen underneath
        draw_frozen_game(screen, paddle, balls, bricks, powerups, game_manager)

        # Draw overlay on top
        draw_pause_screen(screen)

    elif game_manager.state == "game_over":
        # Draw the game over screen, wait for restart
        # Draw the game frozen underneath
        draw_frozen_game(screen, paddle, balls, bricks, powerups, game_manager)

        # Draw overlay on top
        draw_game_over_screen(screen, game_manager, initials)

    elif game_manager.state == "victory":
        # Draw the victory screen - await for action
        draw_victory_screen(screen, game_manager, initials)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()