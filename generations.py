year = int(input('What\'s your year of birth? '))
if year <= 1946:
    print('You are in Traditionalists!')
elif year <= 1964:
    print('You are in Baby Boomers!')
elif year <= 1981:
    print('You are in Generation X!')
elif year <= 1995:
    print('You are in Millenials!')
else:
    print('You are in Generation Z!')
