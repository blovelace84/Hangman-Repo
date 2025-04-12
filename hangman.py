import random
import string

import char

#List of messages
sentences = [
    'Python is awesome',
    "Hangman game in python",
    "Sonic the Hedgehog is my favorite character",
    "Super Monkey Ball",
    "AI is the future. Be ready",
    "Code like a pro"
]

#Pick a random sentence
sentence = random.choice(sentences).lower()

#set up the game with _
guessed_sentence = [char if not char.isalpha() else '_' for char in sentence]
guessed_letters = set()
tries = 6

print("Welcome to Hangman. Ready to play?")
print("Message to guess: " + ' '.join(guessed_sentence))

while tries > 0 and '_' in guessed_sentence:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in sentence:
        print("Correct!")
        for i, char in enumerate(sentence):
            if char == guess:
                guessed_sentence[i] = guess
    else:
        print("Incorrect! Try again.")
        tries -= 1

    print("\nMessage:" + ' '.join(guessed_sentence))
    print("Tries left:", tries)
    print("Guessed letters:", ', '.join(sorted(guessed_letters)))

if '_' not in guessed_sentence:
    print("Congratulations! You won!")
    print(f"\"{sentence}\"")
else:
    print("Sorry, you died! the message was:")
    print(f"\"{sentence}\"")