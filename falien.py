import pygame
import random

class AlienEasy(pygame.sprite.Sprite):
    def __init__(self):  # Evan added speed
        super().__init__()
        self.image = pygame.image.load("assets/images/enemies/enemyBlack1.png")
        self.image = pygame.transform.scale_by(self.image, 0.5) # Adjust size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 550)  # Random x-position
        self.rect.y = -10
        self.speed = 1
        self.point_value = 10

    def update(self):
        self.rect.y += self.speed  # + Because it is moving down from the top of the screen

        #Kills when out of screen
        if self.rect.y > 700:
            self.kill()

class AlienMedium(pygame.sprite.Sprite):
    def __init__(self,all_sprites,alien_lasers_group):  # Evan added speed
        super().__init__()
        self.image = pygame.image.load("assets/images/enemies/enemyBlack5.png")
        self.image = pygame.transform.scale_by(self.image, 0.6) # Adjust size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 550)  # Random x-position
        self.rect.y = -10
        self.speed = 1.5
        self.point_value = 15
        self.all_sprites = all_sprites
        self.alien_lasers_group = alien_lasers_group
        self.shoot_delay = 4500  # Delay between shots (in milliseconds)
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.rect.y += self.speed  # + Because it is moving down from the top of the screen

        # Respawn the alien at the top if it goes off the screen
        # Kills when out of screen
        if self.rect.y > 700:
            self.kill()

            # Check if it's time to shoot a laser
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            self.shoot_laser()

    def shoot_laser(self):
        alien_laser = AlienLaser(self.rect.centerx, self.rect.bottom)
        self.all_sprites.add(alien_laser)
        self.alien_lasers_group.add(alien_laser)

class AlienHard(pygame.sprite.Sprite):
    def __init__(self,all_sprites,alien_lasers_group):  # Evan added speed
        super().__init__()
        self.image = pygame.image.load("assets/images/enemies/enemyRed4.png")
        self.image = pygame.transform.scale_by(self.image, 0.8) # Adjust size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 550)  # Random x-position
        self.rect.y = -10
        self.speed = .9
        self.point_value = 20
        self.all_sprites = all_sprites
        self.alien_lasers_group = alien_lasers_group
        self.shoot_delay = 3000  # Delay between shots (in milliseconds)
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.rect.y += self.speed  # + Because it is moving down from the top of the screen

        # Kills when out of screen
        if self.rect.y > 700:
            self.kill()

        # Check if it's time to shoot a laser
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            self.shoot_laser()

    def shoot_laser(self):
        alien_laser = AlienLaser(self.rect.centerx, self.rect.bottom)
        self.all_sprites.add(alien_laser)
        self.alien_lasers_group.add(alien_laser)

    # Create a new class for the alien's laser
class AlienLaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/lasers/laserRed01.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 4  # Laser's speed

    def update(self):
        self.rect.y += self.speed

        # Remove the laser if it goes off the screen
        if self.rect.y > 650:
            self.kill()