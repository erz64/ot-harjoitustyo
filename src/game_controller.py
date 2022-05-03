import pygame

class GameControl:
    """Class that controls the game

    Attributes:
        level: Class level that is initialized in the app file
        clock: Pygames clock which handles the time in the game
        display: Pygames display which opens the window for the game, initialized in the app file
    """

    def __init__(self, display, level):
        """Class' contructor which initializes class variables

        Args:
            display: window for the game
            level: Class which handles game mechanics
        """
        pygame.init()
        self._level = level
        self._clock = pygame.time.Clock()
        self._display = display
        self._font_1 = pygame.font.SysFont("arial", 24)

    def start(self):
        """Gets called in the app file from main function and starts the program
            Runs until, exited
        """
        while True:
            if self._player_inputs() is False:
                break
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((29, 17, 53))
            self._level.all_sprites.draw(self._display)
            self._level.all_sprites.update()
            if not self._level.check_player_collision():
                break
            self._level.check_bullet_collision()
            self._level.spawn_enemies()
            self._level.spawn_boss()
            self._level.spawn_bullet()
            self._level.boss_attack()
            self._level.is_boss_dead()
            self._score_render()

    def _player_inputs(self):
        """Checks if the game is exited

        Returns:
            True if it isn't, and False if exited
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def _score_render(self):
        """Displays the player's score in the top left corner"""
        stage = self._font_1.render(
            f"Stage: {self._level.stage}", True, (255, 0, 0))
        self._display.blit(stage, (300, 0))
