from datetime import datetime

def days(delta):
# convert string to date object
    fDate = datetime.strptime(fDate, '%Y/%m/%d')
    sDate = datetime.strptime(sDate, '%Y/%m/%d')
    
    delta = sDate - fDate

    print('The difference between your first and second date is', abs(delta), 'days')
fDate = input('Type first date in format 1981/12/2 : ')
sDate = input('Type second date in format 1981/12/2 : ')
