"""
CodeAlpha Python Internship - Task 1: Hangman Game
A simple text-based Hangman game using random, while loop, if-else,
string and lists.
"""

import random

# Small list of 5 predefined words
WORDS = ["python", "program", "computer", "keyboard", "internet"]
MAX_WRONG = 6


def display_word(word, guessed_letters):
    """Show the word with underscores for letters not yet guessed."""
    shown = []
    for letter in word:
        if letter in guessed_letters:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = []   # all letters the player has tried
    wrong_guesses = 0

    print("=== Welcome to Hangman! ===")
    print("Guess the word one letter at a time.")
    print(f"You are allowed {MAX_WRONG} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG:
        print("Word:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "none")
        print(f"Incorrect guesses left: {MAX_WRONG - wrong_guesses}")

        guess = input("Enter a letter: ").lower().strip()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed_letters:
            print("You already guessed that letter.\n")
        else:
            guessed_letters.append(guess)

            if guess in word:
                print("Good guess!\n")
            else:
                wrong_guesses += 1
                print("Wrong guess!\n")

        # Check for a win
        if "_" not in display_word(word, guessed_letters):
            print("Word:", word)
            print("Congratulations! You won!")
            return

    print("Game over! You ran out of guesses.")
    print("The word was:", word)


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for playing. Goodbye!")
            break
        print()


main()
