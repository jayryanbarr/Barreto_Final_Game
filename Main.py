import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 800
#BACKGROUND_COLOR = (0, 0, 0)  # Black

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load your background image
background_image = pygame.image.load("assets/images/background/background.jpg")  # Replace with the path to your background image

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    #screen.fill(BACKGROUND_COLOR)

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
