from random import randint
import os
import pygame


class Boss(pygame.sprite.Sprite):
    """Sprite class for bosses, inherits the pygame sprite class

    Attributes:
        boss_image: loads the original image for the boss
        damaged_boss: changes the original boss image to red when damaged
        image: initializes the surface for the boss
        rect: gets the hitboxes for the rectangle
        rect.x: x-coordinate of the rectangle
        rect.y: y-coordinate of the rectangle
        color: timer which changes the color of the rectangle to red when above zero
        hitpoints: the amount of times the boss needs to be hit before getting destroyed
        move_cooldown: how long until next time the boss moves up or down
        move_duration: how long the boss moves
        direction: in which direction does the boss move
    """

    def __init__(self):
        """Class' constuctor which initializes class variables"""
        super().__init__()
        dirname = os.path.dirname(__file__)
        super().__init__()
        self.boss_image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "boss.png"))
        self.damaged_boss_image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "damaged_boss.png"))
        self.image = self.boss_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300
        self.color = 0
        self.hitpoints = 30
        self.move_cooldown = 0
        self.move_duration = 0
        self.direction = 1

    def update(self):
        """Updates the boss, including movement and changing the color"""
        if self.color > 0:
            self.color -= 1
            self.image = self.damaged_boss_image
        if self.color == 0:
            self.image = self.boss_image
        if self.move_cooldown > 100 and self.move_duration < 150:
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
        """Reduces hitpoints of the boss
        and changes the coloring timer to 10 so player sees when the boss is hit"""
        self.hitpoints -= 1
        self.color = 10
