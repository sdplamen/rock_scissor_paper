test = input('What\'s the name of the test you\'ve just done ?')

if test == 'Python Skills' or test == 'python skills':
    print('Great, that\s it !')
else:
    print('Nope, you do a wrong test.')
score = int(input('What\'re the maximum of the scores ?'))
yourScore = int(input('What\'re your scores ?'))

numberScore = float(yourScore / score)
finalNumber = round(numberScore, 0)
finalPerc = round(float(yourScore / score) * 100, 2)
print('You got', finalPerc, '%')
if finalNumber >= yourScore % 0.9:
    print('You\'re at grade A+')
elif finalNumber >= yourScore % 0.8 and finalNumber <= yourScore % 0.9:
    print('You\'re at grade A')
elif finalNumber >= yourScore % 0.7 and finalNumber <= yourScore % 0.8:
    print('You\'re at grade B')
elif finalNumber >= yourScore % 0.6 and finalNumber <= yourScore % 0.7:
    print('You\'re at grade C')
elif finalNumber >= yourScore % 0.5 and finalNumber <= yourScore % 0.6:
    print('You\'re at grade D')
else:
    print('You\'re at grade U')
