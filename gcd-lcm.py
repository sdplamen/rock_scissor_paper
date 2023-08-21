# Greatest common divisor (GCD) of two positive integers.
'''Algorithm: Step 1: Let  a, b be the two numbers
Step 2: a mod b = R
Step 3: Let a = b and b = R
Step 4: Repeat Steps 2 and 3 until a mod b is greater than 0
Step 5: GCD = a Step 6: Finish'''

def gcd():
    a = int(input('type a digit for GCD: '))
    b = int(input('type a digit for GCD: '))
    print(math.gcd(a, b))
gcd()
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))
a = int(input('type a digit for GCD: '))
b = int(input('type a digit for GCD: '))
print('GCD of', a, 'and', b, 'is',gcd(a, b))

# Least common multiple (LCM) of two positive integers.
def lcm(a, b):
    return (a / gcd(a, b)) * b
a = int(input('type a digit for GCD: '))
b = int(input('type a digit for GCD: '))
print('LCM of', x, 'and', y, 'is', lcm(x, y))
