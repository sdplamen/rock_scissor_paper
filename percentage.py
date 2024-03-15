# show float number of some percentage
def calc():
    perc = a * b / 100
    print(f"That\'s your number {a} \n\tand that\'s its percentage {round(perc, 2)} \n\t\tYour bill is: {round(a + perc, 2)}")
a = float(input('Please type a number: '))
b = float(input('Please type a percentage you want for this number: '))
calc()
