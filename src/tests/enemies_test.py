import unittest
import pygame
from sprites.enemy import Enemy
from sprites.player import Player
from level import Level


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.enemy = Enemy()
        self.level = Level()
        pygame.init()

    def test_enemy_spawn(self):
        pass
