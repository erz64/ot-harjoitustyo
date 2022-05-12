import pygame
from game_controller import GameControl
from level import Level
import database_connection
from event_queue import EventQueue


def main():
    event_queue = EventQueue()
    display = pygame.display.set_mode((1600, 900))
    level = Level()
    connection = database_connection.get_database_connection()
    game_control = GameControl(display, level, connection, event_queue)
    pygame.display.set_caption("Dodge the objects")
    pygame.init()
    game_control.main_menu()
    while game_control.end_screen():
        level = Level()
        game_control = GameControl(display, level, connection, event_queue)
        game_control.main_menu()


if __name__ == "__main__":
    main()
