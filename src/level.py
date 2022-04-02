import pygame
from sprites.player import Player

class Level:
    def __init__(self):
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.load_all_sprites()
        
    def load_all_sprites(self):
        self.all_sprites.add(self.player)
