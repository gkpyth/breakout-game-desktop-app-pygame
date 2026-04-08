import pygame
import math
from settings import *

# Draw the start screen with the game title and text that says Press Space to Start
def draw_start_screen(screen):
    """Draws the start screen with the game title and text that says Press Space to Start"""
    # Set theme
    theme = get_theme()
    screen.fill(theme["background"])

    # Fonts
    title_font = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 80)
    subtitle_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 32)

    # Title with glow
    title_text = "BREAKOUT"
    title_surface = title_font.render(title_text, True, theme["menu_text"])
    title_rect = title_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 50))

    # Draw glow layers behind the title
    glow_color = (0, 80, 160)
    for offset in range (5, 0, -1):
        glow = title_font.render(title_text, True, glow_color)
        glow.set_alpha(40)
        screen.blit(glow, (title_rect.x - offset, title_rect.y + offset))
        screen.blit(glow, (title_rect.x + offset, title_rect.y + offset))

    # Draw the main title
    screen.blit(title_surface, title_rect)

    # Draw pulsing subtitle
    alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
    subtitle_surface = subtitle_font.render("Press Space to Start", True, (180, 200, 220)).convert_alpha()
    subtitle_surface.set_alpha(alpha)
    subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
    screen.blit(subtitle_surface, subtitle_rect)

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
    subtitle_surface = subtitle_font.render(subtitle_text, True, (180, 200, 220)).convert_alpha()
    subtitle_surface.set_alpha(alpha)
    subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
    screen.blit(subtitle_surface, subtitle_rect)

def draw_game_over_screen(screen, score):
    """Draws the game over screen with GAME OVER text, the score, and Press Space to Restart"""
    overlay = pygame.Surface(WINDOW_SIZE)
    overlay.set_alpha(150)
    overlay.fill(get_theme()["pause_screen"])
    screen.blit(overlay, (0, 0))

    # Fonts
    game_over_font = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 64)
    score_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 32)
    subtitle_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)

    # Title
    game_over_text = "GAME OVER"
    game_over_surface = game_over_font.render(game_over_text, True, get_theme()["menu_text"])
    game_over_rect = game_over_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 50))
    screen.blit(game_over_surface, game_over_rect)

    # Score
    score_text = f"Score: {score}"
    score_surface = score_font.render(score_text, True, get_theme()["menu_text"])
    score_rect = score_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    screen.blit(score_surface, score_rect)

    # Subtitle - Pulsing
    subtitle_text = "Press Space to Restart"

    alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
    subtitle_surface = subtitle_font.render(subtitle_text, True, (180, 200, 220)).convert_alpha()
    subtitle_surface.set_alpha(alpha)
    subtitle_rect = subtitle_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
    screen.blit(subtitle_surface, subtitle_rect)

def draw_victory_screen(screen, score):
    """Draws the victory screen with VICTORY! text and Press Space to Play Again"""
    # Set theme
    theme = get_theme()
    screen.fill(theme["background"])

    # Fonts
    title_font = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 80)
    score_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 32)
    subtitle_font = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)

    # Title with glow
    title_text = "VICTORY!"
    title_surface = title_font.render(title_text, True, theme["menu_text"])
    title_rect = title_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 50))

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
    score_text = f"Score: {score}"
    score_surface = score_font.render(score_text, True, get_theme()["menu_text"])
    score_rect = score_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    screen.blit(score_surface, score_rect)

    # Draw pulsing subtitle
    alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 500))
    subtitle_surface = subtitle_font.render("Press Space to Play Again", True, (180, 200, 220)).convert_alpha()
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
    text_surface = text_font.render("Press Space to Launch Ball", True, (180, 200, 220)).convert_alpha()
    text_surface.set_alpha(alpha)
    subtitle_rect = text_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 50))
    screen.blit(text_surface, subtitle_rect)