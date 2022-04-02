import pygame
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill((29, 17, 53))
        pygame.draw.circle(self.image,(0,255,0),(10,10),10)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 450
        self.pos = Vector2(800, 450)
    
    def update(self):
        direction = pygame.mouse.get_pos() - self.pos
        self.pos += direction
        self.rect.center = self.pos