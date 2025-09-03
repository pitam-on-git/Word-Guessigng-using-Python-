# Word Guessing Game 🎮

A simple and fun Python Word Guessing Game inspired by Hangman!  
The program randomly selects a word from a word bank, and you get 10 attempts to guess it letter by letter. Correct guesses reveal the hidden letters, wrong guesses reduce your attempts. Can you solve the word before you run out of tries?

---

## Features

- **Random word selection** from a predefined word bank.
- **10 attempts** to guess the word, one letter at a time.
- **Correct guesses** reveal the letter in the word.
- **Wrong guesses** decrease your remaining attempts.
- **Win** by solving the word before you run out of attempts!

---

## How to Play

1. **Run the script:**  
   Open your terminal and run `python word_guess.py`.

2. **Game instructions:**  
   - The program will show you how many attempts you have left.
   - Enter a letter (a-z) for each guess.
   - Correct guesses reveal the letter(s) in their positions.
   - Incorrect guesses reduce the number of attempts.
   - The game ends when you guess the entire word or run out of attempts.

---

## Example Gameplay

```
Welcome to the Word Guessing Game!

Try to guess the word I'm thinking of!
You have 10 attempts to guess the word.
Please enter only one letter.

Current word: _ _ _ _

Guess a letter: o
Great guess!

Current word: o _ _ _

Guess a letter: h
Wrong guess! Attempts left: 9

...
```

---

## Requirements

- Python 3.x

No external libraries required.

---

## Customization

- Change the word bank by editing the `word_bank` list in `word_guess.py`.
- Adjust the number of attempts by modifying the `attempts` variable.

---

## Author

Made by [pitam-on-git](https://github.com/pitam-on-git)

---

## Idea from Codedex 

By Daniel Li (https://www.codedex.io/projects/build-a-word-guessing-game-with-python)

---
