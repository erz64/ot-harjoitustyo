import pygame
from game_controller import GameControl
from level import Level


def main():
    display = pygame.display.set_mode((1600, 900))
    level = Level()
    game_control = GameControl(display, level)
    pygame.mouse.set_visible(False)
    pygame.init()
    game_control.start()


if __name__ == "__main__":
    main()
