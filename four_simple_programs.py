# Caesar Cipher: encrypting a message
text = input('Enter your message: ')
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Caesar Cipher: decrypting a message
cipher = input('Enter your message: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('A'):
        code = ord('Z')
    text += chr(code)

print(cipher)

# The Numbers Processor
line = input('Enter a line of numbers - separate them with spaces: ')
strings = line=split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print('The total is:', total)
except:
    print(substr, 'is not a number.')

# IBAN Validator
iban = input('Enter IBAN, please: ')
iban = iban.repalce(' ', '')
if not iban.isalnum():
    print('You have entered invalid characters.')
elif len(iban) < 15:
    print('IBAN entered is too short.')
elif len(iban) > 31:
    print('IBAN entered is too long.')
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)
        if iban % 97 == 1:
            print('IBAN entered is valid.')
        else:
            print('IBAN entered is invalid.')
