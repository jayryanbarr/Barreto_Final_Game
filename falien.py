import pygame
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemies/enemyRed1.png")
        self.image = pygame.transform.scale_by(self.image, 0.5) # Adjust size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 550)  # Random x-position
        self.rect.y = 0
        self.speed = 1  # Alien's speed

    def update(self):
        self.rect.y += self.speed  # + Because it is moving down from the top of the screen

        # Respawn the alien at the top if it goes off the screen
        if self.rect.y > 650:
            self.rect.x = random.randint(0, 550)
            self.rect.y = random.randint(0, 50)
