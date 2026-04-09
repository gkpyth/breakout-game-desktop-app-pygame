import pygame
import math

from settings import *

class Ball:
    def __init__(self):
        self.radius = ball_radius
        self.x_pos = ball_x_pos
        self.y_pos = ball_y_pos
        self.x_vel = ball_speed_x
        self.y_vel = ball_speed_y
        self.speed_factor = ball_speed_factor
        self.launched = False
        self.powerup_start = None
        self.powerup_duration = 15000
        self.trail = []

    # Ball drawing
    def draw_ball(self, screen):
        """Draw the ball on the screen"""
        # Draw trail
        offset = self.radius // 4
        for i, (x, y) in enumerate(self.trail):
            alpha = int((i / len(self.trail)) * 120)
            color = get_theme()["ball_trail"]
            trail_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(trail_surface, (color[0], color[1], color[2], 80), (self.radius, self.radius), offset)
            screen.blit(trail_surface, (x - self.radius, y - self.radius))
            offset += 1

        # Draw ball
        pygame.draw.circle(screen, get_theme()["ball"], (self.x_pos, self.y_pos), self.radius)

    # Ball movement
    def move(self, paddle):
        """Move the ball according to its velocity"""
        if not self.launched:
            self.x_pos = paddle.x_pos + paddle.width // 2
            self.y_pos = paddle.y_pos - self.radius
            return
        self.x_pos += self.x_vel * self.speed_factor
        self.y_pos += self.y_vel * self.speed_factor
        self.trail.append((self.x_pos, self.y_pos))
        if len(self.trail) > 10:
            self.trail.pop(0)

    # Ball collision and bouncing logic
    def bounce(self, paddle, sound_manager):
        """Bounce the ball off the walls and the paddle upon collision"""
        if self.x_pos <= 10 + self.radius:
            self.x_vel *= -1
            self.x_pos = 10 + self.radius                           # Nudge away from left wall to avoid infinite bouncing
        if self.x_pos >= WINDOW_SIZE[0] - self.radius - 10:
            self.x_vel *= -1
            self.x_pos = WINDOW_SIZE[0] - self.radius - 10          # nudge away from right wall to avoid infinite bouncing
        if self.y_pos <= 10:
            self.y_vel *= -1
            self.y_pos = 10 + self.radius
        if self.y_pos >= (paddle.y_pos - self.radius) and paddle.x_pos <= self.x_pos <= (paddle.x_pos + paddle.width) and self.y_vel > 0:
            sound_manager.play_paddle_hit()
            hit_position = self.x_pos - (paddle.x_pos + paddle.width // 2)
            normalized = hit_position / (paddle.width / 2)
            normalized = max(-1, min(1, normalized))

            max_angle = math.pi / 3
            angle = math.pi / 2 + normalized * max_angle            # if normalized is +, self.x_vel & self.y_vel should be multiplied by -1

            speed = math.sqrt(self.x_vel**2 + self.y_vel**2)
            self.x_vel = -speed * math.cos(angle)                   # Normalized with + -> speed needs to be inverted
            self.y_vel = -speed * math.sin(angle)                   # Normalized with + -> speed needs to be inverted
            self.y_pos = paddle.y_pos - self.radius                 # Bounce off the paddle

    # Ball reset logic
    def reset(self, paddle):
        """Reset the ball's position and velocity"""
        self.launched = False
        self.x_pos = paddle.x_pos + paddle.width // 2
        self.y_pos = paddle.y_pos - self.radius
        self.x_vel = ball_speed_x
        self.y_vel = ball_speed_y

    def activate_slow_powerup(self, type):
        """Activate the Slow Motion powerup for the ball."""
        if type == "power_up_slow_mo":
            self.speed_factor = 0.7
            self.powerup_start = pygame.time.get_ticks()

    def check_powerup(self):
        if self.powerup_start is not None:
            if pygame.time.get_ticks() - self.powerup_start > self.powerup_duration:
                self.speed_factor = 1
                self.powerup_start = None
