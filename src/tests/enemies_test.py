import unittest
import pygame
from sprites.enemy import Enemy
from sprites.player import Player
from level import Level


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.enemy = Enemy()
        self.level = Level()
        pygame.init()

        
