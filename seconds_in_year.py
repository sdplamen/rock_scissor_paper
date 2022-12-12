second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour
month1 = 31 * day
month2 = 30 * day
noLeapFebr = 28 * day
leapFebr = 29 * day
noLeapYear = (7 * month1) + (4 * month2) + noLeapFebr
leapYear = (7 * month1) + (4 * month2) + leapFebr
noLeapYear = 365 * day
leapYear = 366 * day
currentYear = int(input('What is the year you want to show you in seconds ? '))
if currentYear  % 4 == 0:
    print('This leap year has :', leapYear, 'seconds')
else:
    print('This no leap year has :', noLeapYear, 'seconds')
