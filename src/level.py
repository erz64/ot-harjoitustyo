from random import randint
import pygame
from sprites.enemy import Enemy
from sprites.player import Player
from sprites.boss import Boss
from sprites.bullet import Bullet


class Level:
    def __init__(self):
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bosses = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.bullet_cooldown = 0
        self.boss_cooldown = 0
        self.boss = Boss()
        self.bosses.add(self.boss)
        self.all_sprites.add(self.boss)

    def spawn_enemies(self):
        if self.can_enemy_spawn():
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def check_player_collision(self):
        colliding = pygame.sprite.spritecollide(
            self.player, self.enemies, False)
        end = not colliding
        return end

    def check_bullet_collision(self):
        colliding = pygame.sprite.spritecollide(self.boss, self.bullets, True)
        if colliding:
            self.boss.take_hit()

    def can_enemy_spawn(self):
        if randint(0, 10) == 1:
            return True
        return False

    def spawn_boss(self):
        if self.can_boss_spawn():
            self.boss = Boss()
            self.all_sprites.add(self.boss)
            self.bosses.add(self.boss)

    def can_boss_spawn(self):
        if not self.bosses:
            self.boss_cooldown += 1
        if not self.bosses and self.boss_cooldown >= 2000:
            self.boss_cooldown = 0
            return True
        return False

    def spawn_bullet(self):
        if self.can_bullet_spawn():
            bullet = Bullet(self.player.rect.x - 40, self.player.rect.y+5)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)

    def can_bullet_spawn(self):
        self.bullet_cooldown += 1
        if self.bullet_cooldown >= 30:
            self.bullet_cooldown = 0
            return True
        return False
