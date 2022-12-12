myBill = float(input("What was the original amount ?: "))
tip = int(input("What was the percent of tip to add to the bill: 10 %, 15 %, 20 % ?: "))
totalBill = tip / 100 * myBill
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", round(answer, 2))
