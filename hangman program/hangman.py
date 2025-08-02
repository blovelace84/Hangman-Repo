import random

def display_word(secret_word, guessed_letters):
    return ' '.join([
        letter if letter in guessed_letters or letter == ' ' else '_'
        for letter in secret_word
    ])

def hangman():
    word_list = [
        "python is awesome",
        "I love hangman",
        "coding is a challenge",
        "programming is fun",
        "I am a software developer"
    ]
    secret_word = random.choice(word_list).lower()
    guessed_letters = []
    tries = 6

    print("🎮 Welcome to Hangman!")

    while tries > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            print("Wrong!")
            tries -= 1
        #Winning conditions: All letters guessed
        letters_in_word = set(secret_word.replace(" ", ""))
        if letters_in_word.issubset(set(guessed_letters)):
            print(f"\nYou win! The sentence was: '{secret_word}'")
            break
    else:
        print(f"\n💀 You lose! The word was '{secret_word}'")

# Run the game
hangman()
