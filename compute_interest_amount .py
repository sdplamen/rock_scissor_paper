# FV = I х (1 + (R х T)) where: I = Investment amount R = Interest rate T = Number of years

def futVal(amount, interest, years):
    future_value = amount * ((1 + (0.01 * interest)) ** years)
    print('The future amount is :', round(future_value, 2))
amount = int(input('Type an amount:'))
interest = float(input('Type an interest for this amount:'))
years = int(input('Type how many years for paying amount:'))
futVal(amount, interest, years)
