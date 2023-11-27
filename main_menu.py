import pygame
import sys
def main_menu(screen, font):
    # Load and scale the background image
    background_image = pygame.image.load("assets/images/background/homescreen2.png")
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
    # Create a bright green box for the button
    button_width = 150
    button_height = 50
    button_color = (0, 0, 0)  # Bright green color
    button_x = (screen.get_width() - button_width) // 2  # Center horizontally
    button_y = 10 # Adjust this value to position the button at the top
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    start_button_text = font.render("START GAME", True, (255, 255, 255))
    start_button_rect = start_button_text.get_rect()
    start_button_rect.center = button_rect.center  # Center the text within the button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the button
                if button_rect.collidepoint(event.pos):
                    return  # Return to start the game
        # Draw the background image
        screen.blit(background_image, (0, 0))
        # Draw the bright green box
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(start_button_text, start_button_rect)
        pygame.display.flip()