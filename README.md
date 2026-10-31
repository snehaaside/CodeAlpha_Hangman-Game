# Hangman Game

A simple text-based Hangman game built in Python as part of my CodeAlpha Python Programming Internship.

## About

The computer picks a random word, and the player guesses it one letter at a time. The player is allowed 6 incorrect guesses. If the whole word is guessed before that, the player wins.

## Features

- Picks a random word from a list of 5 predefined words
- Limits incorrect guesses to 6
- Shows the word with blanks for letters not yet guessed
- Shows the letters already guessed
- Handles invalid input and repeated guesses without penalty
- Option to play again after each game
- Console-only, with no graphics or audio

## Concepts Used

- `random` module
- `while` loop
- `if-else` statements
- Strings
- Lists
- Functions

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python hangman.py
```

## Sample Output

```
=== Welcome to Hangman! ===
Guess the word one letter at a time.
You are allowed 6 incorrect guesses.

Word: _ _ _ _ _ _
Guessed letters: none
Incorrect guesses left: 6
Enter a letter: p
Good guess!

Word: p _ _ _ _ _
```

## Author

Kumari Sneha
