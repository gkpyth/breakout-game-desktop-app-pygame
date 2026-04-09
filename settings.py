WINDOW_SIZE = (800, 600)
GAME_TITLE = "Breakout"

current_theme = "dark"

# Color Palette - DARK THEME, LIGHT THEME
DARK_THEME = {
    "background": (15, 15, 25),
    "pause_screen": (10, 10, 20),
    "paddle": (200, 210, 230),
    "ball": (240, 245, 255),
    "ball_trail": (100, 120, 180),
    "menu_text": (220, 225, 235),
    "score_text": (180, 190, 210),
    "lives_text": (180, 190, 210),
    "level_text": (180, 190, 210),
    "brick_border": (40, 42, 55),
    "brick_1hp": (220, 70, 80),
    "brick_2hp": (230, 160, 50),
    "brick_3hp": (60, 170, 220),
    "power_up_grow": (0, 200, 100),
    "power_up_balls": (100, 150, 255),
    "power_up_slow_mo": (200, 100, 255),
    "power_up_life": (255, 100, 150),
}

LIGHT_THEME = {
    "background": (235, 237, 245),
    "pause_screen": (220, 222, 230),
    "paddle": (45, 50, 65),
    "ball": (35, 40, 55),
    "ball_trail": (140, 150, 180),
    "menu_text": (40, 45, 60),
    "score_text": (70, 75, 90),
    "lives_text": (70, 75, 90),
    "level_text": (70, 75, 90),
    "brick_border": (200, 205, 215),
    "brick_1hp": (200, 55, 65),
    "brick_2hp": (210, 140, 40),
    "brick_3hp": (45, 140, 200),
    "power_up_grow": (0, 170, 85),
    "power_up_balls": (70, 120, 230),
    "power_up_slow_mo": (170, 70, 230),
    "power_up_life": (230, 75, 125),
}

# Theme Settings Helper Function
def get_theme():
    """Returns the current theme based on the global variable 'current_theme'."""
    if current_theme == "dark":
        return DARK_THEME
    return LIGHT_THEME

# Toggle Theme Helper Function
def toggle_theme():
    """Toggles the current theme between 'dark' and 'light'."""
    global current_theme
    if current_theme == "dark":
        current_theme = "light"
    else:
        current_theme = "dark"

# Paddle Settings
paddle_width = 100
paddle_height = 20
paddle_x_pos = (WINDOW_SIZE[0] // 2) - paddle_width // 2
paddle_y_pos = WINDOW_SIZE[1] - 30
paddle_move_increment = 10
paddle_speed_factor = 1

# Ball Settings
ball_radius = 10
ball_x_pos = WINDOW_SIZE[0] // 2
ball_y_pos = WINDOW_SIZE[1] - (30 + ball_radius * 2)
ball_speed_factor = 1
ball_speed_x = 0
ball_speed_y = -7

# Brick Settings
brick_width = 76
brick_height = 20
brick_gap = 10
brick_points = {
    1: 10,
    2: 25,
    3: 50,
}

# Game Settings
starting_lives = 3
starting_score = 0
starting_level = 1

# Power-up colors
powerup_types = ["power_up_grow", "power_up_balls", "power_up_slow_mo", "power_up_life"]

powerup_move_increment = 2
powerup_speed_factor = 1
powerup_drop_chance = 0.25

powerup_width = 20
powerup_height = 20
