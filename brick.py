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
        self.just_hit = set()

    # Brick drawing
    def draw_brick(self, screen):
        """Draw the brick on the screen"""
        theme = get_theme()
        if self.hp == 1:
            color = theme["brick_1hp"]
        elif self.hp == 2:
            color = theme["brick_2hp"]
        elif self.hp == 3:
            color = theme["brick_3hp"]
        pygame.draw.rect(screen, color, (self.x_pos, self.y_pos, self.width, self.height))
        pygame.draw.rect(screen, theme["brick_border"], (self.x_pos, self.y_pos, self.width, self.height), 2)

    # Brick collision logic
    def hit(self, ball):
        """Check if the ball collides with the brick"""
        ball_rect = pygame.Rect(ball.x_pos - ball.radius, ball.y_pos - ball.radius, ball.radius * 2, ball.radius * 2)
        brick_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        if ball_rect.colliderect(brick_rect):
            if id(ball) not in self.just_hit:
                self.hp -= 1
                self.just_hit.add(id(ball))
                return True
        else:
            self.just_hit.discard(id(ball))
        return False

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False
