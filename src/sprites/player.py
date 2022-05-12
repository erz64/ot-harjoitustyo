import pygame
from pygame import Vector2


class Player(pygame.sprite.Sprite):
    """Sprite class for player, inherits the pygame sprite class

    Attributes:
        image: initializes the surface for the player
        rect: gets the hitboxes for the rectangle
        rect.x: x-coordinate of the rectangle
        rect.y: y-coordinate of the rectangle
        pos: position of the player
    """

    def __init__(self):
        """Class' constuctor which initializes class variables"""
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((29, 17, 53))
        pygame.draw.circle(self.image, (0, 255, 0), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.pos = Vector2(800, 450)

    def update(self):
        """Updates the player, including movement"""
        direction = pygame.mouse.get_pos() - self.pos
        self.pos += direction
        self.rect.center = self.pos
