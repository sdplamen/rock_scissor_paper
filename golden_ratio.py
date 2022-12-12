import math
pi = 4 * math.atan(1)
print(pi)

pi = math.acos(-1)
print(pi)

# Golden ration (or Rule of Thirds)
math.pi
phi = (1 + math.sqrt(5)) / 2
print(phi)

phi = (1 + 5 ** 0.5) / 2
print(phi)

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

def fib(n):
  if (n == 0) or (n == 1):
    return(1)
  else:
    return fib(n - 1) + fib(n - 2)

for i in range(10):
  print(i + 1, fib(i))
