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
        self.level._boss_cooldown = 1001
        pygame.init()

    def test_player_movement(self):
        pygame.mouse.set_pos(100, 200)
        self.player.update()
        self.assertEqual(self.player.rect.center, pygame.mouse.get_pos())

    def test_player_collision(self):
        self.level._player.rect.x = 30
        self.level._player.rect.y = 300
        self.level.spawn_boss()
        self.assertEqual(self.level.check_player_collision(), False)
