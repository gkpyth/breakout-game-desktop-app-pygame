import pygame

from settings import *

class Brick:
    def __init__(self, x, y, hp):
        self.x_pos = x
        self.y_pos = y
        self.width = brick_width
        self.height = brick_height
        self.max_hp = hp
        self.hp = hp
        self.border_color = brick_border_color
        self.set_brick_color()
        self.just_hit = False

    # Brick color setter - helper function
    def set_brick_color(self):
        """Set the color of the brick based on its health"""
        if self.hp == 1:
            self.color = brick_1hp_color
        elif self.hp == 2:
            self.color = brick_2hp_color
        elif self.hp == 3:
            self.color = brick_3hp_color

    # Brick drawing
    def draw_brick(self, screen):
        """Draw the brick on the screen"""
        self.set_brick_color()
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))
        pygame.draw.rect(screen, self.border_color, (self.x_pos, self.y_pos, self.width, self.height), 2)

    # Brick collision logic
    def hit(self, ball):
        """Check if the ball collides with the brick"""
        ball_rect = pygame.Rect(ball.x_pos - ball.radius, ball.y_pos - ball.radius, ball.radius * 2, ball.radius * 2)
        brick_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        if ball_rect.colliderect(brick_rect):
            if not self.just_hit:
                self.hp -= 1
                self.just_hit = True
                return True
        else:
            self.just_hit = False
        return False

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False
