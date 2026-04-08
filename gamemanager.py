import pygame
from settings import *
from levels import *
from ball import Ball

class GameManager:
    def __init__(self):
        self.lives = starting_lives
        self.score = starting_score
        self.level = starting_level
        self.state = "start"                  # States: start, playing, paused, game_over, victory
        self.font = pygame.font.SysFont("monospace", 24)

    def lose_life(self):
        """Decrease the number of lives by 1"""
        self.lives -= 1

    def update_score(self, max_hp):
        """Update the score"""
        self.score += brick_points[max_hp]

    def next_level(self):
        """Increase the level"""
        self.level += 1

    def game_over(self):
        """Reset the game variables"""
        self.lives = starting_lives
        self.score = starting_score
        self.level = starting_level

    def reset_game(self, paddle):
        """Returns fresh bricks, balls, paddle, and powerups for a new game."""
        self.game_over()
        bricks = create_level(LEVELS[self.level - 1])
        balls = [Ball()]
        powerups = []
        paddle.reset()
        return bricks, balls, powerups

    def draw_hud(self, screen):
        """Draw the HUD on the screen"""
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        screen.blit(lives_text, (15, 20))

        score_text = self.font.render(f"Score: {self.score:05d}", True, (255, 255, 255))
        screen.blit(score_text, (WINDOW_SIZE[0] - score_text.get_width() - 15, 20))

        level_text = self.font.render(f"LEVEL {self.level}", True, (255, 255, 255))
        screen.blit(level_text, ((WINDOW_SIZE[0] - level_text.get_width()) // 2, 20))

    def activate_life_powerup(self, type):
        """Activates the Life powerup for the player."""
        if type == "life":
            self.lives += 1