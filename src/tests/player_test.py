import unittest
import pygame
from pygame import Vector2
from sprites.enemy import Enemy
from sprites.player import Player
from level import Level


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.enemy = Enemy()
        self.level = Level()
        pygame.init()

    def test_player_movement(self):
        pygame.mouse.set_pos(100, 200)
        self.player.update()
        self.assertEqual(self.player.rect.center, pygame.mouse.get_pos())

    def test_player_collision(self):
        pygame.mouse.set_pos(100, 200)
        self.enemy.pos = Vector2(100, 200)
        self.level.all_sprites.add(self.enemy)
        self.level.enemies.add(self.enemy)
        self.level.all_sprites.update()
        self.assertEqual(self.level.check_player_collision(), True)
