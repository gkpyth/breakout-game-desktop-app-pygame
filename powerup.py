import pygame
import random
from settings import *

class PowerUp:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = powerup_width
        self.height = powerup_height
        self.type = random.choice(powerup_types)

    def draw_powerup(self, screen):
        """Draw the powerup on the screen."""
        pygame.draw.rect(screen, get_theme()[self.type], (self.x_pos, self.y_pos, self.width, self.height))

    def paddle_collision(self, paddle):
        """Check if the powerup collides with the paddle."""
        powerup_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        paddle_rect = pygame.Rect(paddle.x_pos, paddle.y_pos, paddle.width, paddle.height)
        if powerup_rect.colliderect(paddle_rect):
            return True
        return False

    def drop_powerup(self):
        """Move the powerup down by 5 pixels."""
        self.y_pos += powerup_move_increment * powerup_speed_factor
