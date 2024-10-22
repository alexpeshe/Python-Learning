import math

figure = input()

area = 0.0

a = float(input())

if figure == 'square':
    area = a*a
    print("%.3f" % area)
elif figure == 'rectange':
    b = float(input())
    area = a*b
    print("%.3f" % a*b)
elif figure == 'circle':
    area = math.pi * a ** 2
    print("%.3f" % area)
elif figure == 'triangle':
    h = float(input())
    area = 1/2 * a * h
    print("%.3f" %  area)

