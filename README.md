# Breakout

A modern Breakout arcade game built with Python and Pygame. Destroy bricks with a bouncing ball, collect power-ups, and climb the leaderboard.

## Features
- Smooth 60 FPS gameplay with Pygame
- Multi-hit bricks (1HP, 2HP, 3HP) with color-coded health
- Paddle-position-based ball bounce angles
- Power-ups (wide paddle, multi-ball, slow ball, extra life)
- Multiple levels with unique brick layouts
- Lives system
- Score tracking and leaderboard (saved to JSON)
- Particle effects on brick destruction
- Ball trail effect
- Sound effects
- Dark/light theme toggle

## Requirements
- Python 3
- Pygame

## Installation
```
pip install -r requirements.txt
```

## How to Run
```
python main.py
```

## How to Play
- Use **Left/Right arrow keys** to move the paddle
- Bounce the ball off the paddle to break bricks
- Don't let the ball fall past the paddle
- Collect power-ups for special abilities
- Clear all bricks to advance to the next level

## Project Structure
```
breakout-game-gui/
├── main.py          # Entry point and game loop
├── settings.py      # Constants, colors, and theme palettes
├── paddle.py        # Paddle class
├── ball.py          # Ball class
├── brick.py         # Brick class
├── levels.py        # Level layouts and brick generation
├── powerup.py       # Power-up class
├── particles.py     # Particle effects
├── ui.py            # Screens (start, pause, game over, leaderboard)
├── sounds.py        # Sound manager
├── scores.json      # Saved high scores
└── assets/
    └── sounds/      # Sound files
```

## Leaderboard
Scores are saved locally to `scores.json`. The leaderboard stores the top 10 scores.

## Limitations
- TBD

## Author
Ghaleb Khadra