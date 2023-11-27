import pygame
import sys

def sub_menu(screen, font):
    # Load and scale the background image
    background_image = pygame.image.load("assets/images/background/submenu.jpg")
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    # Define button properties
    button_width = 300
    button_height = 100
    button_color = (0, 0, 0)  # Green color for the button
    button_x = (screen.get_width() - button_width) // 2  # Center horizontally
    button_y = (screen.get_height() - button_height) // 2  # Center vertically

    # Create a button rect
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Main loop for the sub-menu
    while True:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mouse click is within the button
                    if button_rect.collidepoint(event.pos):
                        return  # Return to start the game

        # Draw the button
        pygame.draw.rect(screen, button_color, button_rect)

        # Add text to the button
        text = font.render('Start Game', True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

        pygame.display.update()


