# Integer values up to and including 3999 into Roman numerals.For example, the Roman numeral representation of 1984 is MCMLXXXIV.
def roman_to_dec(num):
    if num > 3999:
        raise ValueError ('Cannot translate number greater than 3999 !')
    symbols = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_num = ''
    i = 0
    count = list(symbols)
    while num > 0:
        for _ in range(num // count[i]):
            roman_num += symbols[count[i]]
            num -= count[i]
        i += 1
    '''while num > 0:
        for _ in range(num // symbols[i]):
            roman_num += symbols.values(i)
            num -= symbols[i]
        i += 1'''
    print(f'The Roman numeral representation is : {roman_num}')
    return roman_num

num = int(input('Enter a number to convert to roman symbol : '))
roman_to_dec(num)

# convert roman numbers to numerals

int_value = 0
user_input = input("Enter Roman Number: ").upper()

roman = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

for i in range(len(user_input)):
    if user_input[i] in roman:
        if i + 1 < len(user_input) and roman[user_input[i]] < roman[user_input[i + 1]]:
            int_value -= roman[user_input[i]]
        else:
            int_value += roman[user_input[i]]
            print("The integer value of this roman is : ", int_value)
    else:
        print("Invalid input.")

'''if __name__ == '__main__':
    tests = ['I', 'V', 'VII', 'IX', 'X', 'MCMVII', 'CM', 'MCXCIX']
    for i in tests:
        print(f'{i} = {roman(i)}')'''

# Every natural number N lies between two consecutive powers of 2
n = int(input('Enter a number : '))
lower, upper = 0, 0
for x in range(n):
    p = 2 ** x
    if p <= n:
        lower = p
    elif p >= n:
        upper = p
        break
    if lower == upper:
        print(n, 'is a power of 2')
    else:
        print(n, 'lies between', lower, 'and', upper)
