def is_armstrong(num):
    
    num_str = str(num)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

number_to_check = int(input('Enter a number to check for Armstrong number : '))
result = is_armstrong(number_to_check)

if result:
    print(f'{number_to_check} is an Armstrong number.')
else:
    print(f'{number_to_check} is not an Armstrong number.')
    
# check for armstrong number in any range
def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    armstrong_sum = sum(int(digit) ** power for digit in num_str)
    return armstrong_sum == num

def find_armstrong_numbers(start, end):
    armstrong_numbers = []

    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)

    return armstrong_numbers

start_range = int(input('Enter a number to start of range for Armstrong number : '))
end_range = int(input('Enter a number to end of range for Armstrong number : '))

print(f'Armstrong numbers in the range {(start_range, end_range)} are {find_armstrong_numbers(start_range, end_range)}')

# For n-digit numbers – using a while loop
n = int(input('Enter the number of digits : '))
start_range = 10 ** (n - 1)
end_range = 10 ** n

for num in range(start_range, end_range):
    temp = num
    sum_of_powers = 0

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n
        temp //= 10

    if sum_of_powers == num:
        print(num, end = ' ')

# For n-digit numbers – using functions
def is_armstrong(num, power):
    temp = num
    sum_of_powers = 0

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** power
        temp //= 10

    return sum_of_powers == num

n = int(input('Enter the number of digits :'))
start_range = 10 ** (n - 1)
end_range = 10 ** n

for num in range(start_range, end_range):
    if is_armstrong(num, n):
        print(num, end = ' ')

# For n-digit numbers – using recursion
def is_armstrong_recursive(num, power, original_num):
    if num == 0:
        return 0
    digit = num % 10
    return digit ** power + is_armstrong_recursive(num // 10, power, original_num)

def is_armstrong(num, power):
    return is_armstrong_recursive(num, power, num) == num

n = int(input('Enter the number of digits : '))
start_range = 10 ** (n - 1)
end_range = 10 ** n

for num in range(start_range, end_range):
    if is_armstrong(num, n):
        print(num, end = ' ')
