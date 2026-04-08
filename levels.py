from settings import *
from brick import Brick

# Level Layouts

# LEVEL_1 = [
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [2, 2, 2, 2, 2, 2, 2, 2, 2],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]

# Level for testing
LEVEL_1 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]

# LEVEL_2 = [
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [2, 2, 2, 2, 2, 2, 2, 2, 2],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]

# Level for testing
LEVEL_2 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]

# LEVEL_3 = [
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [2, 2, 2, 2, 2, 2, 2, 2, 2],
#     [1, 2, 1, 2, 1, 2, 1, 2, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# Level for testing
LEVEL_3 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]

# LEVEL_4 = [
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [2, 2, 2, 2, 2, 2, 2, 2, 2],
#     [1, 2, 3, 2, 3, 2, 3, 2, 1],
#     [2, 1, 2, 1, 2, 1, 2, 1, 2],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# Level for testing
LEVEL_4 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]

# LEVEL_5 = [
#     [3, 3, 3, 3, 3, 3, 3, 3, 3],
#     [3, 3, 3, 0, 0, 0, 3, 3, 3],
#     [3, 3, 0, 0, 3, 0, 0, 3, 3],
#     [3, 0, 0, 3, 3, 3, 0, 0, 3],
#     [3, 0, 3, 3, 3, 3, 3, 0, 3],
#     [3, 0, 3, 3, 3, 3, 3, 0, 3]
# ]

# Level for testing
LEVEL_5 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]

LEVELS = [LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5]

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
            if brick.hp > 0:
                bricks.append(brick)
    return bricks