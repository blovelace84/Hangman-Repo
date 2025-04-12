import random

sentences = [
    "Python is awesome",
    "Hello world",
    "OpenAI is the future. Be ready",
    "Sonic the Hedgehog is my favorite game",
    "Super Monkey Ball"
    "Hangman game in Python",
    "Code like a pro"
]

sentence = random.choice(sentences).lower()

# Corrected list comprehension
guessed_sentence = [char if not char.isalpha() else '_' for char in sentence]
guessed_letters = set()
tries = 6

print("🎮 Welcome to Sentence Hangman!")
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
        print("Good guess!")
        for i, char in enumerate(sentence):
            if char == guess:
                guessed_sentence[i] = guess
    else:
        print("Wrong guess.")
        tries -= 1

    print("\nMessage: " + ' '.join(guessed_sentence))
    print("Tries left:", tries)
    print("Guessed letters:", ', '.join(sorted(guessed_letters)))
    print("-" * 40)

if '_' not in guessed_sentence:
    print("Congratulations! You won!")
    print(f"\"{sentence}\"")
else:
    print("Game over! You died! The message was:")
    print(f"\"{sentence}\"")
