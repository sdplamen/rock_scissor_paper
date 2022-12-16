import math

def volume(rad):
    volume = (4 / 3 * math.pi * rad ** 3)
    print('The volume of circle is : ', round(volume, 2))
rad = int(input('Type the raduis for the circle : '))
volume(rad)
