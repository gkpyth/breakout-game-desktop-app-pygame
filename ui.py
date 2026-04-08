import pygame
import math

from settings import *

# Draw the start screen with the game title and text that says Press Space to Start
def draw_start_screen(screen, data):
    """Draws the start screen with the game title and text that says Press Space to Start"""
    # Fill screen with background color
    screen.fill(get_theme()["background"])

    # Fonts
    title_font = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 80)
    subtitle_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 32)
    score_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)
    hint_font = pygame.font.Font("assets/fonts/Orbitron-Regular.ttf", 12)

    # Title with glow
    title_text = "BREAKOUT"
    title_surface = title_font.render(title_text, True, get_theme()["menu_text"])
    title_rect = title_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 200))

    # Draw glow layers behind the title
    glow_color = (0, 80, 160)
    for offset in range (5, 0, -1):
        glow = title_font.render(title_text, True, glow_color)
        glow.set_alpha(40)
        screen.blit(glow, (title_rect.x - offset, title_rect.y + offset))
        screen.blit(glow, (title_rect.x + offset, title_rect.y + offset))

    # Draw the main title
    screen.blit(title_surface, title_rect)

    # Draw Leaderboard
    leaderboard_text = "Leaderboard"
    leaderboard_surface = subtitle_font.render(leaderboard_text, True, get_theme()["menu_text"])
    leaderboard_rect = leaderboard_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 100))
    screen.blit(leaderboard_surface, leaderboard_rect)

    if data:
        for i, entry in enumerate(data[:5]):
            y = WINDOW_SIZE[1] // 2 - 10 + i * 30

            rank_surface = score_font.render(f"{i+1}.", True, get_theme()["menu_text"])
            rank_rect = rank_surface.get_rect(center=(WINDOW_SIZE[0] // 2 - 200, y))
            screen.blit(rank_surface, rank_rect)

            initials_surface = score_font.render(entry["initials"], True, get_theme()["menu_text"])
            initials_rect = initials_surface.get_rect(center=(WINDOW_SIZE[0] // 2, y))
            screen.blit(initials_surface, initials_rect)

            score_surface = score_font.render(f"{entry['score']}", True, get_theme()["menu_text"])
            score_rect = score_surface.get_rect(center=(WINDOW_SIZE[0] // 2 + 200, y))
            screen.blit(score_surface, score_rect)

    else:
        score_text = "No scores yet!"
        score_surface = score_font.render(score_text, True, get_theme()["menu_text"])
        score_rect = score_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
        screen.blit(score_surface, score_rect)

    # Draw pulsing subtitle
    alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
    subtitle_surface = subtitle_font.render("Press Space to Start", True, get_theme()["menu_text"]).convert_alpha()
    subtitle_surface.set_alpha(alpha)
    subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 200))
    screen.blit(subtitle_surface, subtitle_rect)

    # Draw hint text
    hint_text = "T - Toggle Theme Light/Dark"
    hint_surface = hint_font.render(hint_text, True, get_theme()["menu_text"])
    hint_rect = hint_surface.get_rect(center=(WINDOW_SIZE[0] - 110, WINDOW_SIZE[1] - 25))
    screen.blit(hint_surface, hint_rect)

def draw_pause_screen(screen):
    """Draws the pause overlay with GAME PAUSED text and Press Space to Continue"""
    overlay = pygame.Surface(WINDOW_SIZE)
    overlay.set_alpha(150)
    overlay.fill(get_theme()["pause_screen"])
    screen.blit(overlay, (0, 0))

    # Fonts
    pause_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 64)
    subtitle_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)

    # Title
    pause_text = "GAME PAUSED"
    pause_surface = pause_font.render(pause_text, True, get_theme()["menu_text"])
    pause_rect = pause_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    screen.blit(pause_surface, pause_rect)

    # Subtitle - Pulsing
    subtitle_text = "Press Esc to Continue"

    alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
    subtitle_surface = subtitle_font.render(subtitle_text, True, get_theme()["menu_text"]).convert_alpha()
    subtitle_surface.set_alpha(alpha)
    subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
    screen.blit(subtitle_surface, subtitle_rect)

def draw_game_over_screen(screen, game_manager, initials):
    """Draws the game over screen with GAME OVER text, the score, and Press Space to Restart"""
    overlay = pygame.Surface(WINDOW_SIZE)
    overlay.set_alpha(150)
    overlay.fill(get_theme()["background"])
    screen.blit(overlay, (0, 0))

    # Fonts
    title_font = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 64)
    score_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 32)
    subtitle_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)
    input_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 46)

    # Title
    title_text = "GAME OVER"
    title_surface = title_font.render(title_text, True, get_theme()["menu_text"])
    title_rect = title_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 100))
    screen.blit(title_surface, title_rect)

    # Score
    score_text = f"Score: {game_manager.score}"
    score_surface = score_font.render(score_text, True, get_theme()["menu_text"])
    score_rect = score_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 30))
    screen.blit(score_surface, score_rect)

    if not game_manager.score_saved:
        subtitle_text = "Enter Initials"
        subtitle_surface = subtitle_font.render(subtitle_text, True, get_theme()["menu_text"])
        subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 30))
        screen.blit(subtitle_surface, subtitle_rect)

        slot_width = 50  # fixed width per slot
        total_width = slot_width * 3
        start_x = (WINDOW_SIZE[0] - total_width) // 2

        for i in range(3):
            char = initials[i] if i < len(initials) else "_"
            char_surface = input_font.render(char, True, get_theme()["menu_text"])
            char_rect = char_surface.get_rect(
                center=(start_x + i * slot_width + slot_width // 2, WINDOW_SIZE[1] // 2 + 80))
            screen.blit(char_surface, char_rect)

    elif pygame.time.get_ticks() - game_manager.score_saved_time < 2000:
        subtitle_text = "Score Saved!"
        subtitle_surface = subtitle_font.render(subtitle_text, True, get_theme()["menu_text"])
        subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
        screen.blit(subtitle_surface, subtitle_rect)

    else:
        # Subtitle - Pulsing
        subtitle_text = "Press Space to Restart"

        alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
        subtitle_surface = subtitle_font.render(subtitle_text, True, (180, 200, 220)).convert_alpha()
        subtitle_surface.set_alpha(alpha)
        subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
        screen.blit(subtitle_surface, subtitle_rect)

def draw_victory_screen(screen, game_manager, initials):
    """Draws the victory screen with VICTORY! text and Press Space to Play Again"""
    # Fill screen with background color
    screen.fill(get_theme()["background"])

    # Fonts
    title_font = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 80)
    score_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 32)
    subtitle_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)
    input_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 46)

    # Title with glow
    title_text = "VICTORY!"
    title_surface = title_font.render(title_text, True, get_theme()["menu_text"])
    title_rect = title_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 100))

    # Draw glow layers behind the title
    glow_color = (0, 160, 80)
    for offset in range(5, 0, -1):
        glow = title_font.render(title_text, True, glow_color)
        glow.set_alpha(40)
        screen.blit(glow, (title_rect.x - offset, title_rect.y + offset))
        screen.blit(glow, (title_rect.x + offset, title_rect.y + offset))

    # Draw the main title
    screen.blit(title_surface, title_rect)

    # Score
    score_text = f"Score: {game_manager.score}"
    score_surface = score_font.render(score_text, True, get_theme()["menu_text"])
    score_rect = score_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 30))
    screen.blit(score_surface, score_rect)

    if not game_manager.score_saved:
        subtitle_text = "Enter Initials"
        subtitle_surface = subtitle_font.render(subtitle_text, True, get_theme()["menu_text"])
        subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 30))
        screen.blit(subtitle_surface, subtitle_rect)

        slot_width = 50  # fixed width per slot
        total_width = slot_width * 3
        start_x = (WINDOW_SIZE[0] - total_width) // 2

        for i in range(3):
            char = initials[i] if i < len(initials) else "_"
            char_surface = input_font.render(char, True, get_theme()["menu_text"])
            char_rect = char_surface.get_rect(
                center=(start_x + i * slot_width + slot_width // 2, WINDOW_SIZE[1] // 2 + 80))
            screen.blit(char_surface, char_rect)

    elif pygame.time.get_ticks() - game_manager.score_saved_time < 2000:
        subtitle_text = "Score Saved!"
        subtitle_surface = subtitle_font.render(subtitle_text, True, get_theme()["menu_text"])
        subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
        screen.blit(subtitle_surface, subtitle_rect)

    else:
        # Subtitle - Pulsing
        subtitle_text = "Press Space to Play Again"

        alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
        subtitle_surface = subtitle_font.render(subtitle_text, True, get_theme()["menu_text"]).convert_alpha()
        subtitle_surface.set_alpha(alpha)
        subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
        screen.blit(subtitle_surface, subtitle_rect)

# Helper Functions for UI
def draw_frozen_game(screen, paddle, balls, bricks, powerups, game_manager):
    paddle.draw_paddle(screen)
    for ball in balls:
        ball.draw_ball(screen)
    for brick in bricks:
        brick.draw_brick(screen)
    for powerup in powerups:
        powerup.draw_powerup(screen)
    game_manager.draw_hud(screen)

def draw_pulsing_ball_release_text(screen):
    """Draws the pulsing text "Press Space to Launch Ball"""
    # Fonts
    text_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)

    # Draw pulsing subtitle
    alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
    text_surface = text_font.render("Press Space to Launch Ball", True, get_theme()["menu_text"]).convert_alpha()
    text_surface.set_alpha(alpha)
    subtitle_rect = text_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
    screen.blit(text_surface, subtitle_rect)
