num = int(input('Enter a number: '))
factorial = 1
if num < 0:
    print('Sorry, factorial does not exist for negative numbers')
elif num == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'The factorial of {num} is {factorial}')

# # #

n = int(input('Enter a number: '))
factorial = 1 if n == 0 else functools.reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)
