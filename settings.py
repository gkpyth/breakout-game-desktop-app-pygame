WINDOW_SIZE = (800, 600)
FPS = 60
GAME_TITLE = "Breakout"

current_theme = "dark"

# Color Palette - DARK THEME, LIGHT THEME
DARK_THEME = {
    "background": (0, 0, 0),
    "paddle": (255, 255, 255),
    "ball": (255, 255, 255),
    "ball_trail": (255, 255, 255),
    "menu_text": (255, 255, 255),
    "score_text": (255, 255, 255),
    "lives_text": (255, 255, 255),
    "brick_border": (255, 255, 255),
    "brick_1hp": (255, 0, 0),
    "brick_2hp": (255, 165, 0),
    "brick_3hp": (255, 255, 0),
    "particles": (255, 255, 255),
    "power_up_grow": (255, 255, 255),
    "power_up_balls": (255, 255, 255),
    "power_up_slow_mo": (255, 255, 255),
    "level_border": (255, 255, 255),
    "hud_area": (255, 255, 255),
}

LIGHT_THEME = {
    "background": (0, 0, 0),
    "paddle": (255, 255, 255),
    "ball": (255, 255, 255),
    "ball_trail": (255, 255, 255),
    "menu_text": (255, 255, 255),
    "score_text": (255, 255, 255),
    "lives_text": (255, 255, 255),
    "brick_border": (255, 255, 255),
    "brick_1hp": (255, 0, 0),
    "brick_2hp": (255, 165, 0),
    "brick_3hp": (255, 255, 0),
    "particles": (255, 255, 255),
    "power_up_grow": (255, 255, 255),
    "power_up_balls": (255, 255, 255),
    "power_up_slow_mo": (255, 255, 255),
    "level_border": (255, 255, 255),
    "hud_area": (255, 255, 255),
}

# Theme Settings Helper Function
def get_theme():
    """Returns the current theme based on the global variable 'current_theme'."""
    if current_theme == "dark":
        return DARK_THEME
    return LIGHT_THEME

# Paddle Settings
paddle_color = get_theme()["paddle"]
paddle_width = 100
paddle_height = 20
paddle_x_pos = (WINDOW_SIZE[0] // 2) - paddle_width // 2
paddle_y_pos = WINDOW_SIZE[1] - 30
paddle_move_increment = 10
paddle_speed_factor = 1

# Ball Settings
ball_color = get_theme()["ball"]
ball_radius = 10
ball_x_pos = WINDOW_SIZE[0] // 2
ball_y_pos = WINDOW_SIZE[1] - (30 + ball_radius * 2)
ball_speed_factor = 1
ball_speed_x = 5
ball_speed_y = -5

# Brick Settings
brick_default_color = get_theme()["brick_1hp"]
brick_border_color = get_theme()["brick_border"]
brick_1hp_color = get_theme()["brick_1hp"]
brick_2hp_color = get_theme()["brick_2hp"]
brick_3hp_color = get_theme()["brick_3hp"]
brick_width = 76
brick_height = 20
brick_gap = 10
