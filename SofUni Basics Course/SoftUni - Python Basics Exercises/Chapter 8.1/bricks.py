import math

x = int(input())
w = int(input())
m = int(input())

rounds = math.ceil(x / (w*m)) # to round the number

print(round(rounds))

