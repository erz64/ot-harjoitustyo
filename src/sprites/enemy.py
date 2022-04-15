from random import randint
import pygame
from pygame import Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((29, 17, 53))
        self.rect = self.image.get_rect()
        self.velocity = 0.003
        self.pos = Vector2(-20, randint(-200, 1100))
        self.dir = pygame.Vector2(3000, randint(100, 800))

    def update(self):
        pygame.draw.circle(self.image, (255, 28, 28), (10, 10), 10)
        direction = self.dir - self.pos
        self.pos += direction * self.velocity
        self.rect.center = self.pos
        if self.rect.left >= 1700:
            pygame.sprite.Sprite.kill(self)
