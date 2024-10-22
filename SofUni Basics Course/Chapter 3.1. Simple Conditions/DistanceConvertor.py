number = float(input())
source_value = input().lower()
exit_value = input().lower()

# Convert to meters first
if source_value == 'mm':
    number = number / 1000
elif source_value == 'cm':
    number = number / 100
elif source_value == 'km':
    number = number * 1000
elif source_value == 'in':
    number = number * 0.0254
elif source_value == 'yd':
    number = number * 0.9144
elif source_value == 'ft':
    number = number * 0.3048
elif source_value == 'mi':
    number = number * 1609.344

# Convert from meters to desired unit
if exit_value == 'mm':
    number = number * 1000
elif exit_value == 'cm':
    number = number * 100
elif exit_value == 'km':
    number = number / 1000
elif exit_value == 'in':
    number = number / 0.0254
elif exit_value == 'yd':
    number = number / 0.9144
elif exit_value == 'ft':
    number = number / 0.3048
elif exit_value == 'mi':
    number = number / 1609.344

print(f'{number:.6f} {exit_value}')