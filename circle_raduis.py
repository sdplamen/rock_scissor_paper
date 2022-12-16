import math

def circle(rad):
    area = math.pi * rad ** 2
    print(round(area, 2))
rad = int(input('Type the raduis for the circle : '))
circle(rad)
