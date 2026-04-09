import pygame
import random

from settings import *

class Particle:
    def __init__(self, brick):
        self.x_pos = brick.x_pos + brick.width / 2
        self.y_pos = brick.y_pos + brick.height / 2
        self.x_vel = random.randint(-3, 3)
        self.y_vel = random.randint(-3, 3)
        self.radius = 15
        self.alpha = 255

    def update(self):
        """Move, shrink, and fade the particle"""
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.radius -= 1
        self.alpha -= 5

    def draw(self, screen):
        """Draw the particle on the screen"""
        if self.radius > 0:
            surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            color = get_theme()["brick_1hp"]
            pygame.draw.circle(surface, (color[0], color[1], color[2], self.alpha), (self.radius, self.radius), self.radius)
            screen.blit(surface, (self.x_pos - self.radius, self.y_pos - self.radius))

    def is_dead(self):
        """Return True if the particle is no longer visible"""
        if self.alpha <= 0:
            return True
        return False
