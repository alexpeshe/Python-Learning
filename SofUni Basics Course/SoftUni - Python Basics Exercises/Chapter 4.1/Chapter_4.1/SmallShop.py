# read the input

product = input()
town = input()
quantity = float(input())

result = 0

if town == 'sofia':
    if product == 'coffee':
        result = quantity * 0.50
    elif product == 'water':
        result = quantity * 0.80
    elif product == 'beer':
        result = quantity * 1.20
    elif product == 'sweets':
        result = quantity * 1.45
    elif product == 'peanuts':
        result = quantity * 1.60

elif town == 'varna':
    if product == 'coffee':
        result = quantity * 0.45
    elif product == 'water':
        result = quantity * 0.70
    elif product == 'beer':
        result = quantity * 1.10
    elif product == 'sweets':
        result = quantity * 1.35
    elif product == 'peanuts':
        result = quantity * 1.55


elif town == 'plovdiv':
    if product == 'coffee':
        result = quantity * 0.40
    elif product == 'water':
        result = quantity * 0.70
    elif product == 'beer':
        result = quantity * 1.15
    elif product == 'sweets':
        result = quantity * 1.30
    elif product == 'peanuts':
        result = quantity * 1.50

print(result)