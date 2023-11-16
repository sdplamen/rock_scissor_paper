# convert fahrenheit to celsius
a = float(input('Enter temperature in Fahrenheit:'))
celsius = (a - 32) * 5/9

print('Your temperature in Fahrenheit', round(a, 2) ,'\n\tis equal to', round(celsius, 2),'in Celsius')

# convert celsius to fahrenheit
a = float(input('Enter temperature in Celsius:'))
celsius = (a * 1.8) + 32

print('Your temperature in Celsius', round(a, 2) ,'\n\tis equal to', round(celsius, 2),'in Fahrenheit')
