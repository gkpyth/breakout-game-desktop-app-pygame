import pygame

MUSIC_TRACKS = [
    "assets/sounds/breakout_track1.mp3",
    "assets/sounds/breakout_track2.mp3",
    "assets/sounds/breakout_track3.mp3",
    "assets/sounds/breakout_track4.mp3",
]

class SoundManager:
    def __init__(self):
        # Set up mixer
        self.current_track = 0
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

        # Load sounds
        self.brick_hit = pygame.mixer.Sound("assets/sounds/brick_hit.wav")
        self.brick_destroy = pygame.mixer.Sound("assets/sounds/brick_destroyed.wav")
        self.paddle_hit = pygame.mixer.Sound("assets/sounds/paddle_hit.wav")
        self.powerup_spawn = pygame.mixer.Sound("assets/sounds/powerup_spawn.wav")
        self.powerup_catch = pygame.mixer.Sound("assets/sounds/powerup_catch.wav")
        self.ball_launch = pygame.mixer.Sound("assets/sounds/ball_launch.wav")
        self.lose_life = pygame.mixer.Sound("assets/sounds/lose_life.wav")
        self.game_over = pygame.mixer.Sound("assets/sounds/game_over.wav")
        self.victory = pygame.mixer.Sound("assets/sounds/victory.wav")
        self.level_complete = pygame.mixer.Sound("assets/sounds/level_complete.wav")

        # Set volume
        self.brick_hit.set_volume(0.3)
        self.brick_destroy.set_volume(0.3)
        self.paddle_hit.set_volume(0.3)
        self.powerup_spawn.set_volume(0.3)
        self.powerup_catch.set_volume(0.6)
        self.ball_launch.set_volume(0.3)
        self.lose_life.set_volume(0.3)
        self.game_over.set_volume(0.5)
        self.victory.set_volume(0.5)
        self.level_complete.set_volume(0.7)

    def play_brick_hit(self):
        self.brick_hit.play()

    def play_brick_destroyed(self):
        self.brick_destroy.play()

    def play_paddle_hit(self):
        self.paddle_hit.play()

    def play_powerup_spawn(self):
        self.powerup_spawn.play()

    def play_powerup_catch(self):
        self.powerup_catch.play()

    def play_ball_launch(self):
        self.ball_launch.play()

    def play_lose_life(self):
        self.lose_life.play()

    def play_game_over(self):
        self.game_over.play()

    def play_victory(self):
        self.victory.play()

    def play_level_complete(self):
        self.level_complete.play()

    def start_music(self):
        pygame.mixer.music.load(MUSIC_TRACKS[self.current_track])
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(MUSIC_TRACKS)
        self.start_music()

    def stop_music(self):
        pygame.mixer.music.stop()
