# hex() function
def hec(dec):
    dec = int(dec)
    print(f'The hexadecimal form of {dec} is ' + hex(dec))
dec = input('Type a decimal number : ')
hec(dec)

# format string
def conv(hex):
    hex = int(hex)
    print('{0:x}'.format(hex))
hex = input('Type a decimal number : ')
conv(hex)
