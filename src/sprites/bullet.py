import pygame


class Bullet(pygame.sprite.Sprite):
    """Sprite class for bullets, inherits the pygame sprite class

    Attributes:
        image: initializes the surface for the bullet
        rect: gets the hitboxes for the rectangle
        rect.x: x-coordinate of the rectangle
        rect.y: y-coordinate of the rectangle
    """

    def __init__(self, x, y):
        """Class' constuctor which initializes class variables"

        Args:
            x: x-coordinate of the rectangle
            y: y-coordinate of the rectangle
        """
        super().__init__()
        self.image = pygame.Surface([20, 10])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Updates the bullet, including movement,
        and destroying itself when it reaches the end of screen"""
        self.rect.x -= 10
        if self.rect.left <= 0:
            pygame.sprite.Sprite.kill(self)
