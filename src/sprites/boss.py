import pygame
from random import randint


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
        self.move_cooldown = 0
        self.move_duration = 0
        self.direction = 1

    def update(self):
        if self.color > 0:
            self.color -= 1
            self.image.fill((255, 28, 28))
        if self.color == 0:
            self.image.fill((0, 0, 0))
        if self.move_cooldown > 100 and self.move_duration < 100:
            if self.move_duration == 0:
                random = randint(0, 1)
                if random == 0:
                    if self.rect.y < 700:
                        self.direction = 1
                    else:
                        self.direction = -1
                elif random == 1:
                    if self.rect.y > 200:
                        self.direction = -1
                    else:
                        self.direction = 1
            self.rect.move_ip(0, self.direction)
            self.move_duration += 1
        if self.move_duration >= 100:
            self.move_cooldown = 0
            self.move_duration = 0
        self.move_cooldown += 1

    def take_hit(self):
        self.hitpoints -= 1
        if self.hitpoints <= 0:
            pygame.sprite.Sprite.kill(self)
        self.color = 5
