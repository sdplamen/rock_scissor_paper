# Amicable pairs (a, b) are integers where the sum of the proper divisors of a is equal to the sum of the proper divisors of b
# In number theory, proper divisors of a positive integer are the positive integers that divide into that number evenly (without leaving a remainder) but exclude the number itself.

def sum_proper_division(n):
    division_sum = 1
    limit = int(n ** 0.5) + 1

    for i in range(2, limit):
        if n % i == 0:
            division_sum += i
            if i != n // i:
                division_sum += n // i
    return division_sum
def find_amicable_pairs(limit):
    amicable_pairs = []
    for a in range(2, limit):
        b = sum_proper_division(a)
        if a < b and sum_proper_division(b) == a:
            pair = (a, b)
            amicable_pairs.append(pair)
    return amicable_pairs

limit = 5000
amicable_pairs = find_amicable_pairs(limit)
for pair in amicable_pairs:
    print(pair)
