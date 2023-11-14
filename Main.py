import pygame
from fspaceship import Player

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 650
BACKGROUND_COLOR = (0, 0, 0)  # Black to be behind the png when blit

# Creates the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Loads background image
background_image = pygame.image.load("assets/images/background/background.jpg")

#Sprite Int
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background_image, (0, 0))

    #Updates locations
    all_sprites.update()

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()

