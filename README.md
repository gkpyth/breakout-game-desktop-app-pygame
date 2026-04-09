# Breakout

A modern Breakout arcade game built with Python and Pygame. Destroy bricks with a bouncing ball, collect power-ups, and climb the leaderboard.

## Features
- Smooth 60 FPS gameplay with Pygame
- Multi-hit bricks (1HP, 2HP, 3HP) with color-coded health
- Paddle-position-based ball bounce angles
- Power-ups (wide paddle, multi-ball, slow ball, extra life)
- 10 levels with unique brick layouts and increasing difficulty
- Lives system
- Score tracking and leaderboard with arcade-style initials entry (saved to JSON)
- Ball trail effect
- Sound effects and background music with multi-track cycling
- Dark/light theme toggle (press T)

## Requirements
- Python 3
- Pygame

## Installation
```
pip install -r requirements.txt
```

## Sound Files
Sound files are not included in this repository due to licensing restrictions. To enable audio, add your own `.wav` or `.ogg` files to `assets/sounds/` with the following names:

- `brick_hit.wav` — Brick hit sound
- `brick_destroy.wav` — Brick destroyed sound
- `paddle_hit.wav` — Ball hits paddle
- `powerup_spawn.wav` — Power-up appears
- `powerup_catch.wav` — Power-up collected
- `ball_launch.wav` — Ball launched from paddle
- `lose_life.wav` — Life lost
- `game_over.wav` — Game over
- `victory.wav` — All levels cleared
- `level_complete.wav` — Level completed
- `track1.wav`, `track2.wav`, etc. — Background music tracks

If you don't have sound files, comment out the `SoundManager` calls in `main.py` to run the game without audio.

Free game sounds can be found at [OpenGameArt](https://opengameart.org) and [Freesound](https://freesound.org).

## How to Run
```
python main.py
```

## How to Play
- Use **Left/Right arrow keys** to move the paddle
- Press **Space** to launch the ball
- Bounce the ball off the paddle to break bricks
- Don't let the ball fall past the paddle
- Collect power-ups for special abilities
- Clear all bricks to advance to the next level
- Press **T** to toggle dark/light theme
- Press **Esc** to pause/unpause

## Project Structure
```
breakout-game-gui/
├── main.py            # Entry point and game loop
├── settings.py        # Constants, colors, and theme palettes
├── paddle.py          # Paddle class
├── ball.py            # Ball class
├── brick.py           # Brick class
├── levels.py          # Level layouts and brick generation
├── powerup.py         # Power-up class
├── gamemanager.py     # Game state, lives, score, and level management
├── leaderboard.py     # Leaderboard load/save functions
├── ui.py              # Screens (start, pause, game over, victory, leaderboard)
├── sounds.py          # Sound manager class
├── scores.json        # Saved high scores
└── assets/
    ├── fonts/         # Game fonts
    └── sounds/        # Sound files (not included, see above)
```

## Leaderboard
Scores are saved locally to `scores.json`. The leaderboard stores the top 10 scores and displays the top 5 on the start screen. Enter your 3-letter initials after each game to save your score.

## Limitations
- Desktop only (no web or mobile version)
- Keyboard controls only (no mouse support)
- Leaderboard is local (no online or shared scores)
- Sound files not included (must be sourced separately)

## Author
Ghaleb Khadra