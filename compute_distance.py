import math
x1 = int(input('Type x1 coordinate :'))
x2 = int(input('Type x2 coordinate :'))
y1 = int(input('Type y1 coordinate :'))
y2 = int(input('Type y2 coordinate :'))

p = [x1, x2]
q = [y1, y2]

print(math.dist(p, q))
