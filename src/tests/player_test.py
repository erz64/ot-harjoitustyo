import unittest
import pygame
from sprites.player import Player
import app


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
    
    def test_player_movement(self):
        pygame.init()
        pygame.mouse.set_pos(100, 200)
        self.player.update()
        self.assertEqual(self.player.rect.center, pygame.mouse.get_pos())