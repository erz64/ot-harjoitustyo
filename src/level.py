from random import randint
import pygame
from sprites.enemy import Enemy
from sprites.player import Player
from sprites.boss import Boss
from sprites.bullet import Bullet
from sprites.boss_attack import BossAttack


class Level:
    """ Class which handles spawning of sprites, collision check and difficulty increase

        Attributes:
            player: The object player is controlling
            all_sprites: Sprite group which contains all the sprites
            enemies: Sprite group containing enemies
            bosses: Sprite group containing bosses
            bullets: Sprite group containing bullets
            boss_attacks: Sprite group containing bosses_attacks
            bullet_cooldown: The delay between each bullet spawned
            boss_cooldown: The delay between each boss spawned
            boss_attack_cooldown: The delay between boss' each attack
            stage: The current stage of the game
            score: Score achieved during the game
            boss: placeholder until the first boss spawns
        """

    def __init__(self):
        """Classes contructor which initializes the class variables"""
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bosses = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()
        self.boss_attacks = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.bullet_cooldown = 0
        self.boss_cooldown = 0
        self.boss_attack_cooldown = 0
        self.stage = 1
        self.score = 0
        self.boss = 0

    def spawn_enemies(self):
        """Checks if enemy can spawn conditions are met, if they are, create a new enemy"""
        if self.can_enemy_spawn(self.stage):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def can_enemy_spawn(self, stage):
        """Randomizes condtition if an enemy can spawn

        Args:
            stage: Takes the current stage of the game and uses it for randomizing

        Returns:
            True, if randomizing hits, and False if not
        """
        if stage <= 3:
            difficulty = 50 - stage*10
        elif 3 < stage <= 6:
            difficulty = 20 - stage*2
        elif 6 < stage <= 9:
            difficulty = 10 - stage
        else:
            difficulty = 0
        if difficulty == 0:
            return True
        if randint(0, difficulty) == 1:
            return True
        return False

    def spawn_boss(self):
        """Checks if boss can spawn conditions are met, if they are, create a new boss"""
        if self.can_boss_spawn():
            self.boss = Boss()
            self.all_sprites.add(self.boss)
            self.bosses.add(self.boss)

    def can_boss_spawn(self):
        """Determines if a boss can spawn

        Returns:
            True, if no bosses in the game and enough time has passed, False otherwise
        """
        if not self.bosses:
            self.boss_cooldown += 1
        if not self.bosses and self.boss_cooldown >= 1000:
            self.boss_cooldown = 0
            return True
        return False

    def spawn_bullet(self):
        """Checks if bullet can spawn conditions are met,
        if they are, create a new moving bullet starting from the player"""
        if self.can_bullet_spawn():
            bullet = Bullet(self.player.rect.x - 40, self.player.rect.y+5)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)

    def can_bullet_spawn(self):
        """Determines if a bullet can spawn

        Returns:
            True if there is a boss in the game,
            and delay between the last bullet is long enough,
            False, if no bosses in the game or cooldown still going on
        """
        if not self.bosses:
            return False
        self.bullet_cooldown += 1
        if self.bullet_cooldown >= 30:
            self.bullet_cooldown = 0
            return True
        return False

    def boss_attack(self):
        """Checks if boss attack can spawn conditions are met,
        if they are, create a new attack at random width coming from the top"""
        if self.can_boss_attack_happen():
            attack = BossAttack(randint(200, 1700))
            self.all_sprites.add(attack)
            self.enemies.add(attack)
            self.boss_attacks.add(attack)

    def can_boss_attack_happen(self):
        """Determine if a boss attack can happen

        Returns:
            True, if the delay between the last attack is long enough,
            and there is a boss in the game,
            False, if no boss in the game or cooldown still active
        """
        if not self.bosses:
            return False
        self.boss_attack_cooldown += 1
        if self.boss_attack_cooldown >= 30:
            self.boss_attack_cooldown = 0
            return True
        return False

    def check_player_collision(self):
        """Checks if player collides with any enemies including boss attacks

        Returns:
            True, if it nothing is colliding, and False if they are
        """
        colliding = pygame.sprite.spritecollide(
            self.player, self.enemies, False)
        return not colliding

    def check_bullet_collision(self):
        """Checks if bullets are colliding with the boss

        Returns:
            True, if they are colliding,
            and False if they are not colliding or no bosses in the game
        """
        if len(self.bosses) != 0:
            colliding = pygame.sprite.spritecollide(
                self.boss, self.bullets, True)
            if colliding:
                self.boss.take_hit()
                return True
        return False

    def is_boss_dead(self):
        """Checks if there are bosses in the game

            If there is bosses in the game, check its hitpoints,
            if below zero, destroy the boss and increase the stage
        """
        if len(self.bosses) != 0:
            if self.boss.hitpoints <= 0:
                pygame.sprite.Sprite.kill(self.boss)
                self.stage += 1
