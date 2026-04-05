from settings import *
from brick import Brick

LEVEL_1 = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3],
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def create_level(layout):
    """Create a list of Brick objects from a layout."""
    x_offset = 18
    y_offset = 70
    bricks = []
    for row, list in enumerate(layout):
        for col, hp in enumerate(list):
            x = x_offset + col * (brick_width + brick_gap)
            y = y_offset + row * (brick_height + brick_gap)
            brick = Brick(x, y, hp)
            bricks.append(brick)
    return bricks