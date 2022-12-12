import random

a = random.randint(0, 51)
print('Guess a number from 0 to 50: ')

for guessNum in range(1, 7):
    print('Take a guess: ')
    guess = int(input())

    if guess < a:
        print('Your guess is low!')
    elif guess > a:
        print('Your guess is high!')
    else:
        break
if guess == a:
    print('Great! You guess number in ' + str(guessNum) + ' guesses.')
else:
    print('Nope. The number for guess was: ' + str(guessNum))

num = random.randint(0, 1000000)
score = 0
for i in range(1000000):
    guess = int(input('Guess the number between 0 and 1 000 000\n'))
    if guess < num:
        print('Your guess is low. Try again.')
        score += 1
    elif guess > num:
        print('Your guess is high. Try again.')
        score += 1
    else:
        print('Great, you won in', score, 'guesses')
        break
