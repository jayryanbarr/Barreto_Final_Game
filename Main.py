import pygame
from fspaceship import Player
from falien import Alien


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 650
BACKGROUND_COLOR = (0, 0, 0)  # Black to be behind the png when blit
FPS = 60
background_image = pygame.image.load("assets/images/background/background.jpg")
alien_spawn_timer = 0

# Creates the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Space Invaders")

#Sprites

#Sprite for main spaceship
all_sprites = pygame.sprite.Group()
player = Player() #fspaceship
all_sprites.add(player)

#Sprite For Aliens
alien_group = pygame.sprite.Group()
alien1 = Alien() #fspaceship
alien_group.add(alien1)

#Game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Calcultes time every frame
    clock.tick(FPS)
    period = clock.tick(FPS)/1000 #From milliseconds to seconds
    print(f"Period: {period}")
    # Draw background
    screen.blit(background_image, (0, 0))


    #Alien Spawner
    alien_spawn_timer = alien_spawn_timer + period
    print(f"Alien Spawn Timer: {alien_spawn_timer}") #For Debugging
    if alien_spawn_timer >= 2:  #Spawn rate
        alien = Alien()
        alien_group.add(alien)
        alien_spawn_timer = 0

    #Updates locations
    alien_group.update()
    all_sprites.update()

    # Draw all sprites
    all_sprites.draw(screen)
    alien_group.draw(screen)

    pygame.display.set_caption(f"Space Shooters {clock.get_fps()}")
    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()

