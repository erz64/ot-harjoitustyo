import sys
import pygame


class GameControl:
    """Class that controls the game

    Attributes:
        level: Class level that is initialized in the app file
        clock: Pygames clock which handles the time in the game
        display: Pygames display which opens the window for the game, initialized in the app file
        connection: Database connection, initialized in the app file
    """

    def __init__(self, display, level, connection, event_queue):
        """Class' contructor which initializes class variables

        Args:
            display: Window for the game
            level: Class which handles game mechanics
            connection: Connection to the database
            event_queue: Class which returns players inputs
        """
        pygame.init()
        self._connection = connection
        self._level = level
        self._clock = pygame.time.Clock()
        self._event_queue = event_queue
        self._display = display
        self._font_1 = pygame.font.SysFont("arial", 24)
        self._font_2 = pygame.font.SysFont("arial", 50)

    def start(self):
        """Gets called in the main menu  function when player starts the game,
        this starts the program, runs until exited or player loses the game
        """
        pygame.mouse.set_visible(False)
        while True:
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((29, 17, 53))
            self._level.all_sprites.draw(self._display)
            self._level.all_sprites.update()
            self._level.check_bullet_collision()
            self._level.spawn_enemies()
            self._level.spawn_boss()
            self._level.spawn_bullet()
            self._level.boss_attack()
            self._level.is_boss_dead()
            self._score_render()
            self._player_inputs()
            if not self._level.check_player_collision():
                break

    def _player_inputs(self):
        """Checks if the game is exited

        Returns:
            True if it isn't, and False if exited
        """
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._pausing_screen()


    def _score_render(self):
        """Displays the player's score in the top left corner"""
        stage = self._font_1.render(
            f"Stage: {self._level.stage}", True, (255, 0, 0))
        self._display.blit(stage, (300, 0))

    def main_menu(self):
        """ Main menu where player can start the game and see highest stage """
        button_text = self._font_1.render("Start game!", True, (0, 0, 0))
        highscore = self._font_1.render(
            f"Your highest stage: {self._get_highscores()}", True, (255, 0, 0))
        game_instructions = self._font_1.render(
            "Welcome to Dodge the objects! Move your player with your mouse. Good luck!", True, (255, 0, 0))
        self._display.fill((29, 17, 53))
        button = pygame.draw.rect(
            self._display, (0, 200, 87), [650, 420, 130, 50])
        self._display.blit(highscore, [50, 50])
        self._display.blit(game_instructions, [300, 350])
        self._display.blit(button_text, button)
        pygame.display.update()
        start = False
        while True:
            x, y = pygame.mouse.get_pos()
            for event in self._event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and button.collidepoint((x, y)):
                        start = True
            if start:
                break
        self.start()

    def end_screen(self):
        """End screen for when player dies in the game

        Returns:
            True, if player presses the button to return to main menu,
            False, if player closes the game
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO highscores (stage) VALUES (?)", (self._level.stage,))
        self._connection.commit()
        pygame.mouse.set_visible(True)
        game_over = self._font_2.render(
            f"Game over! You reached stage {self._level.stage}", True, (255, 0, 0))
        button_text = self._font_1.render("Back to main menu", True, (0, 0, 0))
        self._display.fill((29, 17, 53))
        self._display.blit(game_over, [390, 300])
        button = pygame.draw.rect(
            self._display, (0, 200, 87), [650, 420, 220, 50])
        self._display.blit(button_text, button)
        pygame.display.update()
        while True:
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and button.collidepoint((x, y)):
                        return True

    def _get_highscores(self):
        """Get highest stage player has gotten to

        Returns:
            Highest stage from the highscores database
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(stage) from highscores")
        stage = cursor.fetchone()[0]
        return stage

    def _pausing_screen(self):
        paused_text = self._font_2.render("Game paused. Press ESC again to continue", True, (255, 0, 0))
        self._display.fill((29, 17, 53))
        self._display.blit(paused_text, [270, 300])
        self._level._paused = 1
        pygame.display.update()
        while True:
            for event in self._event_queue.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return