import pygame
import sys

def help_menu(screen, font):
    # Load and scale the background image
    background_image = pygame.image.load("assets/images/background/helpmenu.jpg")
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    # Back Button
    button_width = 200
    button_height = 50
    button_color = (0, 0, 0)
    button_x = (screen.get_width() - button_width) // 2
    button_y = 500
    back_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    #Sound
    click_sound = pygame.mixer.Sound("assets/sounds/click.wav")

    # Main loop for the help menu
    while True:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    click_sound.play()
                    return  # Return to the previous menu

        # Draw the back button
        pygame.draw.rect(screen, button_color, back_button_rect)

        # Add text to the back button
        back_text = font.render('Back', True, (255, 255, 255))
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)
        pygame.display.set_caption(f"Space Invaders Help Menu")

        pygame.display.update()
