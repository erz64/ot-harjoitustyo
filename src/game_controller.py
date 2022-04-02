import pygame


class GameControl:
    def __init__(self, display, level):
        self._level = level
        self._clock = pygame.time.Clock()
        self._display = display
    
    def start(self):
        while True:
            if self._player_inputs() == False:
                break
            self._level.all_sprites.draw(self._display)
            self._level.all_sprites.update()
            pygame.display.update()
            self._clock.tick(60)
            self._display.fill((29, 17, 53))

            
    
    def _player_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.QUIT:
                return False
            