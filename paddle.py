import pygame

from settings import *

class Paddle:
    def __init__(self):
        self.color = paddle_color
        self.width = paddle_width
        self.height = paddle_height
        self.x_pos = paddle_x_pos
        self.y_pos = paddle_y_pos
        self.move_increment = paddle_move_increment
        self.speed_factor = paddle_speed_factor

    # Paddle drawing
    def draw_paddle(self, screen):
        """Draw the paddle on the screen"""
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))

    # Paddle movement
    def move(self):
        """Move the paddle left or right taking into account a 10 pixel margin"""
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.x_pos >= 20:
            self.x_pos -= self.move_increment * self.speed_factor
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x_pos <= WINDOW_SIZE[0] - self.width - 20:
            self.x_pos += self.move_increment * self.speed_factor
