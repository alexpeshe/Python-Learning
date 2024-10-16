number = float(input())

source_value = input().lower()
exit_value = input().lower()

if source_value == 'mm':
    number = number * 1000
elif source_value == 'cm':
    number = number * 100
elif source_value == 'km':
    number = number / 0.001
elif source_value == 'in':
    number = number * 39.3700787
elif source_value == 'yd':
    number = number * 1.0936133
elif source_value == 'ft':
    number = number * 3.2808399
elif source_value == 'mi':
    number = number / 0.000621371192

print(f'{number} {exit_value}')
