import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/lasers/laserBlue01.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 8 # Laser's speed

    def update(self):
        self.rect.y -= self.speed

        # Remove the laser if it goes off the screen
        if self.rect.y < 0:
            self.kill()

    def play_laser_sound(self):
        laser_sound = pygame.mixer.Sound("Assets/Sounds/lasershot.wav")
        # Play the laser sound when firing
        laser_sound.play()
