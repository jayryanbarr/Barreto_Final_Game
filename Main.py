import pygame
from fspaceship import Player
from falien import Alien
from flaser import Laser


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 650
BACKGROUND_COLOR = (0, 0, 0)  # Black to be behind the png when blit
FPS = 60
background_image = pygame.image.load("assets/images/background/background.jpg")
alien_spawn_timer = 0
explosion_sound = pygame.mixer.Sound("Assets/Sounds/explosion2.wav")
pygame.mixer.music.load('Assets/Sounds/Spaceship.mp3')


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

#Sprite group for the lasers
lasers_group = pygame.sprite.Group()


# Play the background music on a loop
pygame.mixer.music.set_volume(0.8) # Makes music less loud
pygame.mixer.music.play(-1)

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
    #print(f"Period: {period}")
    # Draw background
    screen.blit(background_image, (0, 0))


    #Alien Spawner
    alien_spawn_timer = alien_spawn_timer + period
    #print(f"Alien Spawn Timer: {alien_spawn_timer}") #For Debugging
    if alien_spawn_timer >= 2:  #Spawn rate
        alien = Alien()
        alien_group.add(alien)
        alien_spawn_timer = 0

    #Collision of laser and alines
    #Detects collisons, checks the first and second group. True kills the groups aka makes disappear
    hits = pygame.sprite.groupcollide(alien_group, lasers_group, True, True)
    if hits:
        explosion_sound.play()  # Play the explosion sound when a collision occurs

    # Handle player's spaceship shooting lasers By top arrow key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        now = pygame.time.get_ticks()
        if now - player.last_shot > player.shoot_delay:
            player.last_shot = now
            laser = Laser(player.rect.centerx, player.rect.top)
            lasers_group.add(laser)
            all_sprites.add(laser)
            # Play the laser sound
            laser.play_laser_sound()

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

