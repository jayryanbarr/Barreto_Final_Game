import pygame
import sys

def handle_game_over(screen, fontgame, fontscore ,score):
    game_over_text = fontgame.render("Game Over", True , (255, 0, 0)) #Creates 'Game Over'
    game_over_rect = game_over_text.get_rect() #Rectangular Bounding Box
    game_over_rect.center = (screen.get_width() // 2, screen.get_height() // 2) #Centers Box using integer division '//'

    score_text = fontscore.render(f"TOTAL SCORE: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(game_over_text, game_over_rect) #blits text surface on screen
        screen.blit(score_text, score_rect)
        pygame.display.flip() #updates display to show "Game Over"
