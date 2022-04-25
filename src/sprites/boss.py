import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 300])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300
        self.color = 0
        self.hitpoints = 10

    def update(self):
        if self.color > 0:
            self.color -= 1
            self.image.fill((255, 28, 28))
        if self.color == 0:
            self.image.fill((0, 0, 0))

    def take_hit(self):
        self.hitpoints -= 1
        if self.hitpoints <= 0:
            pygame.sprite.Sprite.kill(self)
        self.color = 5
