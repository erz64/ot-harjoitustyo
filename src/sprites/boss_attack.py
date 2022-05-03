import os
import pygame



class BossAttack(pygame.sprite.Sprite):
    """Sprite class for bosses, inherits the pygame sprite class

    Attributes:
        dirname: location the boss_attack.py file
        image: surface of the attack
        rect: gets the hitboxes for the rectangle
        rect.x: x-coordinate of the rectangle
        rect.y: x-coordinate of the rectangle
    """

    def __init__(self, x):
        """Class' constuctor which initializes class variables

        Args:
            x: x-coordinate of the rectangle
        """
        dirname = os.path.dirname(__file__)
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "blade.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def update(self):
        """Updates the boss' attacks, including moving it down the screen,
        and destroying it when it reaches the bottom
        """
        self.rect.y += 5
        if self.rect.bottom >= 1000:
            pygame.sprite.Sprite.kill(self)
