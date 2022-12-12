import random, sys

Category = 'Animals'
Words = 'Ant Baboon Badger Bat Bear Beaver Camel Cat Clam Cobra Cougar Coyote Crow Deer Dog Donkey Duck Eagle Ferret Fox Frog Goat Goose Hawk Lion Lizard Llama Mole Monkey Moose Mouse Mule Newt Otter Owl Panda Parrot Pigeon Python Rabbit Ram Rat Raven Rhino Salmon Seal Shark Sheep Skunk Sloth Snake Spider Stork Swan Tiger Toad Trout Turkey Turtle Weasel Whale Wolf Wombat Zebra'.split()

Hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def main():
    print('Hangman')

    # Setup variables for a new game:
    missedLetters = []  # List of incorrect letter guesses.
    correctLetters = []  # List of correct letter guesses.
    secretWord = random.choice(Words)  # The word the player must guess.

    while True:  # Main game loop.
        drawHangman(missedLetters, correctLetters, secretWord)
        # Let the player enter their letter guess:
        guess = getPlayerGuess(missedLetters + correctLetters)
        if guess in secretWord:
            # Add the correct guess to correctLetters:
            correctLetters.append(guess)

            # Check if the player has won:
            foundAllLetters = True  # Start off assuming they've won.
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
            # There's a letter in the secret word that isn't
            # yet in correctLetters, so the player hasn't won:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break  # Break out of the main game loop.
        else:
            # The player has guessed incorrectly:
            missedLetters.append(guess)
        # Check if player has guessed too many times and lost. (The
        # "- 1" is because we don't count the empty gallows in
        # Hangman_pics.)
        if len(missedLetters) == len(Hangman_pics) - 1:
            drawHangman(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!')
            print('The word was "{}"'.format(secretWord))
            break
            
def drawHangman(missedLetters, correctLetters, secretWord):
    """Draw the current state of the hangman, along with the missed and
    correctly-guessed letters of the secret word."""
    print(Hangman_pics[len(missedLetters)])
    print('The category is:', Category)
    print()

    # Show the incorrectly guessed letters:
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # Display the blanks for the secret word (one blank per letter):
    blanks = ['_'] * len(secretWord)

    # Replace blanks with correctly guessed letters:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Show the secret word with spaces in between each letter:
    print(' '.join(blanks))

def getPlayerGuess(alreadyGuessed):
    """Returns the letter the player entered. This function makes sure
    the player entered a single letter they haven't guessed before."""
    while True:  # Keep asking until the player enters a valid letter.
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
