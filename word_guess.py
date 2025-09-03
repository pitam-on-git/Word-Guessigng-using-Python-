import random
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)

print("""\nWelcome to the Word Guessing Game!\n
Try to guess the word I'm thinking of!\n
You have 10 attempts to guess the word.\n
Please enter only one letter.\n
""")

guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  while True:
    guess = input('Guess a letter: ').lower()
    if len(guess) == 1 and guess.isalpha():
        break
    print('Please enter only one letter !!!!')

  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
    print('Great guess!')
    
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))

  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the word: \n' + word)
    break

if attempts == 0 and '_' in guessedWord:
  print('\nYou\'ve run out of attempts! The word was: \n' + word)