import pygame

from settings import *

class Paddle:
    def __init__(self):
        self.width = paddle_width
        self.height = paddle_height
        self.x_pos = paddle_x_pos
        self.y_pos = paddle_y_pos
        self.move_increment = paddle_move_increment
        self.speed_factor = paddle_speed_factor
        self.powerup_start = None
        self.powerup_duration = 15000

    # Paddle drawing
    def draw_paddle(self, screen):
        """Draw the paddle on the screen"""
        pygame.draw.rect(screen, get_theme()["paddle"], (self.x_pos, self.y_pos, self.width, self.height))

    # Paddle movement
    def move(self):
        """Move the paddle left or right taking into account a 10 pixel margin"""
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.x_pos >= 20:
            self.x_pos -= self.move_increment * self.speed_factor
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x_pos <= WINDOW_SIZE[0] - self.width - 20:
            self.x_pos += self.move_increment * self.speed_factor

    def reset(self):
        """Reset the paddle's position to the starting position"""
        self.x_pos = paddle_x_pos
        self.y_pos = paddle_y_pos

    def reset_powerup(self):
        self.width = paddle_width
        self.powerup_start = None

    def activate_wide_powerup(self, type):
        """Activate the Wide Paddle powerup for the paddle."""
        if type == "power_up_grow":
            self.width = paddle_width * 1.5
            self.powerup_start = pygame.time.get_ticks()

    def check_powerup(self):
        if self.powerup_start is not None:
            if pygame.time.get_ticks() - self.powerup_start > self.powerup_duration:
                self.width = paddle_width
                self.powerup_start = None
