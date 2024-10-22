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

'''

Converting to meters:
For units smaller than a meter (mm, cm), we divide to convert to meters.
For units larger than a meter (km, mi, etc.), we multiply to convert to meters.

Converting from meters:
For units smaller than a meter (mm, cm), we multiply to convert from meters.
For units larger than a meter (km, mi, etc.), we divide to convert from meters.

The logic is based on the relationship between the units and meters:
1 meter = 1000 mm, so to convert mm to m, divide by 1000; to convert m to mm, multiply by 1000
1 km = 1000 m, so to convert km to m, multiply by 1000; to convert m to km, divide by 1000
This pattern holds for all the conversions. The operations (multiply or divide) are inverses when going to meters versus coming from meters.

'''