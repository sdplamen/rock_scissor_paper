from datetime import datetime

fDate = input('Type first date in format 1981/12/2 : ')
sDate = input('Type second date in format 1981/12/2 : ')

# convert string to date object
fDate = datetime.strptime(fDate, '%Y/%m/%d')
sDate = datetime.strptime(sDate, '%Y/%m/%d')

delta = sDate - fDate
print('# 9')
print('The difference between your first and second date is', delta, 'days')
