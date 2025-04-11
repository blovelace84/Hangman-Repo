import pygame

#Initialize pygame
if not pygame.get_init():
    pygame.init()

#Add Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Add colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (150, 150, 150)

#Add fonts
TITLE_FONT = pygame.font.Font(None, 74)
BUTTON_FONT = pygame.font.Font(None, 48)
WORD_FONT = pygame.font.Font(None, 36)

#Add game states
MENU = 0
EASY = 1
MEDIUM = 2
HARD = 3