import unittest
import pygame
from sprites.bullet import Bullet
from sprites.player import Player
from sprites.boss import Boss
from level import Level


class TestBoss(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.level = Level()
        self.level._boss_cooldown = 1001
        self.level.spawn_boss()
        pygame.init()
    
    def test_stage_increases_when_boss_dies(self):
        self.level._boss.hitpoints = 1
        self.level._boss.take_hit()
        self.level.is_boss_dead()
        self.assertEqual(self.level.stage, 2)
    
    def test_check_collision_between_boss_and_bullet(self):
        self.bullet = Bullet(0, 300)
        self.level._bullets.add(self.bullet)
        self.assertEqual(self.level.check_bullet_collision(), True)
    
    def test_boss_will_move(self):
        self.level._boss.move_cooldown = 101
        self.level._boss.update()
        self.assertNotEqual(self.level._boss.rect.y, 300)
    
    def test_boss_will_stop_moving(self):
        self.level._boss.move_cooldown = 101
        self.level._boss.move_duration = 101
        self.assertEqual(self.level._boss.rect.y, 300)

        

