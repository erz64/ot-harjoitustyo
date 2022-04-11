from random import randint
import pygame
from sprites.enemy import Enemy
from sprites.player import Player


class Level:
    def __init__(self):
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def spawn_enemies(self):
        if self.can_enemy_spawn():
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def check_collision(self):
        colliding = pygame.sprite.spritecollide(
            self.player, self.enemies, False)
        end = not colliding
        print(end)
        return end

    def can_enemy_spawn(self):
        if randint(0, 10) == 1:
            return True
        return False
