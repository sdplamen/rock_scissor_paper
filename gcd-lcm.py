# Greatest common divisor (GCD) of two positive integers.
'''Algorithm: Step 1: Let  x, y be the two numbers
Step 2: x mod y = R
Step 3: Let x = y and y = R
Step 4: Repeat Steps 2 and 3 until x mod y is greater than 0
Step 5: GCD = x Step 6: Finish'''

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, (x % y))
x = 13
y = 137
print('GCD of', x, 'and', y, 'is',gcd(x, y))

# Least common multiple (LCM) of two positive integers.
def lcm(x, y):
    return (x / gcd(x, y)) * y
x = 4
y = 112
print('LCM of', x, 'and', y, 'is', lcm(x, y))
