import pygame
import random
import sys
from fspaceship import Player
from falien import AlienEasy, AlienMedium, AlienHard
from flaser import Laser
from game_over import handle_game_over
from main_menu import main_menu

# Initialize Pygame
pygame.init()

# Constants / Initializing
WIDTH, HEIGHT = 600, 650
BACKGROUND_COLOR = (0, 0, 0)  # Black to be behind the png when blit
FPS = 60
background_image = pygame.image.load("assets/images/background/background.jpg")
alien_spawn_timer = 0
explosion_sound = pygame.mixer.Sound("Assets/Sounds/explosion2.wav")
pygame.mixer.music.load('Assets/Sounds/Spaceship.mp3')
score = 0

# Constants for alien spawning thresholds
ALIEN_EASY_THRESHOLD = 50
ALIEN_MEDIUM_THRESHOLD = 100
ALIEN_HARD_THRESHOLD = 150

# Creates the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Sprite for main spaceship
all_sprites = pygame.sprite.Group()
player = Player() #fspaceship
all_sprites.add(player)

#Sprite For Aliens
alien_group = pygame.sprite.Group()

#Sprite group for the lasers
lasers_group = pygame.sprite.Group()

# Play the background music on a loop
#Evan Prince Showed me how to do this.
pygame.mixer.music.set_volume(0.8) # Makes music less loud
pygame.mixer.music.play(-1)

# Game clock
clock = pygame.time.Clock()

#Font for the score display
font_path = "assets/fonts/Airstream.ttf"
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 60)
font3 = pygame.font.Font(None, 40)
fontscore =  pygame.font.Font(font_path, 24)
titlefont = pygame.font.Font(font_path, 40)

# Functions:

# Function to check if an alien is out of bounds
def any_alien_out_of_bounds(alien_group, screen_height=650):
    return any(alien.rect.y > screen_height for alien in alien_group)

# Function to check if the spaceship collides with an alien
def spaceship_collision():
    return pygame.sprite.spritecollide(player, alien_group, False)

# Game loop Booleans
running = True
game_over = False
in_main_menu = True

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

    if in_main_menu:
        main_menu(screen, titlefont)  # Show the main menu
        in_main_menu = False  # Once "Start" is clicked, exit the main menu
    #GAME LOGIC
    if not game_over:
        #Alien Spawner - Concept from Evan Prince
        alien_spawn_timer = alien_spawn_timer + period
        #Score Within Easy Threshold
        if score <= ALIEN_EASY_THRESHOLD and alien_spawn_timer >= 2:
            num_aliens = random.choice([1, 3])
            for i in range(num_aliens):
                alien = AlienEasy()
                alien_group.add(alien)
            alien_spawn_timer = 0
        #Score Within Medium Threshold
        elif score <= ALIEN_MEDIUM_THRESHOLD and score > ALIEN_EASY_THRESHOLD and alien_spawn_timer > 1.2:
            # Randomly select between AlienEasy and AlienMedium
            random_difficulty = random.choice(["easy", "medium"])
            if random_difficulty == "easy":
                num_aliens = random.choice([1, 4])
                for i in range(num_aliens):
                    alien = AlienEasy()
                    alien_group.add(alien)
                alien_spawn_timer = 0
            else:
                num_aliens = random.choice([1, 3])
                for i in range(num_aliens):
                    alien = AlienMedium()
                    alien_group.add(alien)
                alien_spawn_timer = 0
        #Score Within Hard Threshold
        elif score >= ALIEN_MEDIUM_THRESHOLD and alien_spawn_timer > 1:
            # Randomly select between all three alien types
            random_difficulty = random.choice(["easy", "medium", "hard"])
            if random_difficulty == "easy":
                num_aliens = random.choice([2, 5])
                for i in range(num_aliens):
                    alien = AlienEasy()
                    alien_group.add(alien)
                alien_spawn_timer = 0
            elif random_difficulty == "medium":
                num_aliens = random.choice([2, 3])
                for i in range(num_aliens):
                    alien = AlienMedium()
                    alien_group.add(alien)
                alien_spawn_timer = 0
            else:
                num_aliens = random.choice([1, 3])
                for i in range(num_aliens):
                    alien = AlienHard()
                    alien_group.add(alien)
                alien_spawn_timer = 0

        #Collision of laser and alines
        #Detects collisons, checks the first and second group. True kills the groups aka makes disappear
        hits = pygame.sprite.groupcollide(alien_group, lasers_group, True, True)
        #creates a dictionary of values of sprites
        if hits:
            for alien_hit in hits.keys():
                for laser_hit in hits[alien_hit]:
                    score += alien_hit.point_value
            explosion_sound.play()  # Play the explosion sound when a collision occurs

        #Game Over
        if any_alien_out_of_bounds(alien_group, HEIGHT) or spaceship_collision():
            game_over = True  # Set the game_over flag to True
            handle_game_over(screen, font2, font1, score)   # Call the game over function

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

    # Display the score in the top left corner
    score_text = fontscore.render(f"SCORE: {score}", True, (255, 255, 255)) #True smoothes pixels
    screen.blit(score_text, (10, 10)) #Renders with location (10,10)

    #Caption
    pygame.display.set_caption(f"Space Shooters {clock.get_fps()}")
    # Update the display
    pygame.display.flip()



# Quit the game
pygame.quit()
sys.exit()
