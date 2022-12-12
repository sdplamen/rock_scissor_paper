# Zero Division Error
try:
    y = 1 / 0
except ZeroDivisionError:
    print('Oooops...')

print('THE END')

# Arithmetic Error
try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")
print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
print("THE END.")

# Exception is raised inside a function
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print('Arithmetic problem!')
    return None

badFun(0)

print("THE END.")

# Exception is raised outside a function
def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# raise instruction may be used inside the except branch
def badFun(n):
    try:
        return n / 0
    except:
        print('I did it again!')
        raise

try:
    badFun(0)
except ArithmeticError:
    print('I see!')

print("THE END.")

# assert instruction in action
import math

x = float(input('Enter a number:'))
assert x >= 0.0

x = math.sqrt(x)

print(x)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ix = 0
doit = True

while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False
print('Done')
