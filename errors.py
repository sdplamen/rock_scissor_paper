# Errors, failures, and other plagues
# Anything that can go wrong, go wrong

import math

x = float(input('Enter x:'))
y = math.sqrt(x)

print('Ther square roff of', x, 'equals to:', round(y, 2))

firstNumber = int(input('Enter the first number:'))
secondNumber = int(input('Enter the second number:'))

if secondNumber != 0:
    print(firstNumber / secondNumber)
else:
    print('This operation cannot be done!')

print('THE END')

# but Python prefers
firstNumber = int(input('Enter the first number:'))
secondNumber = int(input('Enter the second number:'))

try:
    print(firstNumber / secondNumber)
except:
    print('This operation cannot be done!')

print('THE END')

try:
    print('1')
    x = 1 / 0
    print('2')
except:
    print('oh dear, something went wrong...')

print('3')

try:
    x = int(input('Enter a number: '))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print('You cannot divide by zero, sorry.')
except ValueError:
    print('You must enter an integer value.')
except:
    print('Oh dear, something went worng...')

print('THE END')
