import pygame
import sys

def handle_game_over(screen, fontgame, fontscore ,score):
    # Game Over Text
    game_over_text = fontgame.render("Game Over", True , (255, 0, 0)) #Creates 'Game Over'
    game_over_rect = game_over_text.get_rect() #Rectangular Bounding Box
    game_over_rect.center = (screen.get_width() // 2, screen.get_height() // 2 - 50) #Centers Box using integer division '//'

    #Total Score Text
    score_text = fontscore.render(f"TOTAL SCORE {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)

    # Back to Sub Menu Text
    button_text = fontscore.render("Back to Menu", True, (255, 255, 255))
    button_rect = button_text.get_rect()
    button_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 100)

    # Sound
    click_sound = pygame.mixer.Sound("assets/sounds/click.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    click_sound.play()
                    return True  # Return to indicate button was pressed

        screen.blit(game_over_text, game_over_rect) #blits text surface on screen
        screen.blit(score_text, score_rect)
        screen.blit(button_text, button_rect)
        pygame.display.set_caption(f"Space Invaders Game Over")
        pygame.display.flip() #updates display to show "Game Over"
