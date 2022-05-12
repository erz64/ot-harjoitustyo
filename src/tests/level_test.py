import unittest
import pygame
from level import Level


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level()
        pygame.init()
    
    def test_bullet_doesnt_spawn_if_no_bosses(self):
        self.level._bullet_cooldown = 31
        self.level.spawn_bullet()
        self.assertEqual(len(self.level._bullets), 0)
    
    def test_bullet_spawn_if_boss_alive(self):
        self.level._boss_cooldown = 1001
        self.level.spawn_boss()
        self.level._bullet_cooldown = 31
        self.level.spawn_bullet()
        self.assertEqual(len(self.level._bullets), 1)
    
    def test_enemies_will_spawn(self):
        self.level.stage = 10
        self.level.spawn_enemies()
        self.assertEqual(len(self.level._enemies), 1)

    def test_boss_attacks_will_spawn_if_boss_alive(self):
        self.level._boss_cooldown = 1001
        self.level.spawn_boss()
        self.level._boss_attack_cooldown = 31
        self.level.boss_attack()
        self.assertEqual(len(self.level._boss_attacks), 1)
