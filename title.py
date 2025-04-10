import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hangman Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Fonts
title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 48)
word_font = pygame.font.Font(None, 36)

# Game states
MENU = 0
GAME = 1
game_state = MENU

def choose_word():
    """Chooses a random word from a predefined list."""
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(words).lower()

def display_word(secret_word, guessed_letters):
    """Displays the current state of the word with guessed letters revealed."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    """Draws a button and handles mouse clicks."""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    color = inactive_color

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        color = active_color
        if click[0] == 1 and action is not None:
            action()

    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = button_font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def game_loop():
    """The main game loop."""
    global game_state
    secret_word = choose_word()
    word_length = len(secret_word)
    guessed_letters = set()
    attempts_left = 6

    running = True
    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_state == GAME:
                    if event.unicode.isalpha():
                        guess = event.unicode.lower()
                        if guess not in guessed_letters:
                            guessed_letters.add(guess)
                            if guess not in secret_word:
                                attempts_left -= 1

        if game_state == GAME:
            word_display = display_word(secret_word, guessed_letters)
            word_text = word_font.render(word_display, True, black)
            word_rect = word_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
            screen.blit(word_text, word_rect)

            attempts_text = word_font.render(f"Attempts left: {attempts_left}", True, black)
            attempts_rect = attempts_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
            screen.blit(attempts_text, attempts_rect)

            if "_" not in word_display:
                win_text = title_font.render("You Win!", True, green)
                win_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
                screen.blit(win_text, win_rect)
                draw_button("Back to Menu", screen_width // 2 - 100, screen_height - 150, 200, 50, (200, 200, 200), (150, 150, 150), lambda: setattr(globals(), 'game_state', MENU))
            elif attempts_left <= 0:
                lose_text = title_font.render(f"You Lose! Word was: {secret_word}", True, black)
                lose_rect = lose_text.get_rect(center=(screen_width // 2, screen_height // 2 - 150))
                screen.blit(lose_text, lose_rect)
                draw_button("Back to Menu", screen_width // 2 - 100, screen_height - 150, 200, 50, (200, 200, 200), (150, 150, 150), lambda: setattr(globals(), 'game_state', MENU))

        pygame.display.flip()

    pygame.quit()

def main_menu():
    """Displays the main menu with a start button."""
    global game_state
    running = True
    while running:
        screen.fill(white)

        title_text = title_font.render("Hangman", True, black)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        screen.blit(title_text, title_rect)

        draw_button("Start Game", screen_width // 2 - 100, screen_height // 2, 200, 50, (200, 200, 200), (150, 150, 150), lambda: setattr(globals(), 'game_state', GAME))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main_menu()