import pygame

from settings import *

class Ball:
    def __init__(self):
        self.color = ball_color
        self.radius = ball_radius
        self.x_pos = ball_x_pos
        self.y_pos = ball_y_pos
        self.x_vel = ball_speed_x
        self.y_vel = ball_speed_y
        self.speed_factor = ball_speed_factor

    # Ball drawing
    def draw_ball(self, screen):
        """Draw the ball on the screen"""
        pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    # Ball movement
    def move(self):
        """Move the ball according to its velocity"""
        self.x_pos += self.x_vel * self.speed_factor
        self.y_pos += self.y_vel * self.speed_factor

    # Ball collision and bouncing logic
    def bounce(self, paddle):
        """Bounce the ball off the walls and the paddle upon collision"""
        if self.x_pos <= 10 or self.x_pos >= WINDOW_SIZE[0] - self.radius - 10:
            self.x_vel *= -1
        if self.y_pos <= 10:
            self.y_vel *= -1
        if self.y_pos >= (paddle.y_pos - self.radius) and paddle.x_pos <= self.x_pos <= (paddle.x_pos + paddle.width) and self.y_vel > 0:
            self.y_vel *= -1

    # Ball reset logic
    def reset(self, paddle):
        """Reset the ball's position and velocity"""
        if self.y_pos > WINDOW_SIZE[1] - self.radius:
            self.x_pos = ball_x_pos
            self.y_pos = ball_y_pos
            self.x_vel = ball_speed_x
            self.y_vel = ball_speed_y