x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

''' 
Формули за намиране на страните на правоъгълник със абсолютна стойност
a = abs(x2 - x1)
b = abs(y1 - y2)
'''

# Поради особеностите на кординатната система и когатосе решават задачи от кординатен тип
# Винаги се почва от минуса, тоест от вътре на вън

if (y >= y1 and y <= y2) and (x >= x1 and x <= x2):
    print('Inside')
else:
    print('Outside')