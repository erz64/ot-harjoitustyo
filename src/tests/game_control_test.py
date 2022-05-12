import unittest
import pygame
from level import Level
from game_controller import GameControl
import database_connection


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class TestGameControl(unittest.TestCase):
    def setUp(self):
        self.display = pygame.display.set_mode((1600, 900))
        self.connection = database_connection.get_database_connection()
        self.level = Level()

    def test_start(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE),
                  StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE)]
        game = GameControl(self.display, self.level,
                           self.connection, StubEventQueue(events))
        game.start()
        self.assertEqual(self.level._paused, 1)
