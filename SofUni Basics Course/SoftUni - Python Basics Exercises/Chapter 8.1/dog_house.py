x = float(input())  # Width/length of house
y = float(input())  # Side length of house
h = float(input())  # Height of triangular roof section


# Front and back walls (subtracting door area)
front_back_wall = x*x*2 - 1.2*2     # Total area minus door (1.2m²)

# Side walls (subtracting windows)
side_walls = x*y*2 - 1.5*1.5*2      # Total area minus windows (1.5m²)

# Roof calculations
roof_side_parts = x*y*2             # Rectangle parts of roof
side_roof = (x*h)/2                 # Triangular parts of roof


# Red paint needed (for roof) - 4.3m² per liter
red = (front_back_wall + roof_side_parts)/4.3

# Green paint needed (for walls) - 3.4m² per liter
green = (side_walls+front_back_wall)/3.4


# Two different ways to format output to 2 decimal places
print(f"{green:.2f}")               # Using f-string
print('{0:.2f}'.format(red))        # Using .format()

"""
Key Points:
----------------------------------------------------------
All inputs are converted to float for decimal calculations

Areas are calculated considering:

Door area (1.2m²)

Window areas (1.5m²)

Roof triangular sections

Paint coverage:

Green paint: 3.4m² per liter

Red paint: 4.3m² per liter

Results are formatted to 2 decimal places

Recommendations
Add input validation

Consider adding comments for clarity

Use more descriptive variable names

Consider creating functions for different calculations

Add error handling for negative inputs
"""

"""
Also ways to format in python:
-------------------------------
1. Using F-strings (Recommended modern approach)

number = 3.14159265359

# 2 decimal places
print(f"{number:.2f}")  # Output: 3.14

# 3 decimal places
print(f"{number:.3f}")  # Output: 3.142

# 4 decimal places
print(f"{number:.4f}")  # Output: 3.1416

# 6 decimal places
print(f"{number:.6f}")  # Output: 3.141593

----------------------------------------------
2. Using .format() method

number = 3.14159265359

# 2 decimal places
print("{:.2f}".format(number))  # Output: 3.14

# 3 decimal places
print("{:.3f}".format(number))  # Output: 3.142

# 4 decimal places
print("{:.4f}".format(number))  # Output: 3.1416

-------------------------------------------------
3. Using % operator (Older style)

number = 3.14159265359

# 2 decimal places
print("%.2f" % number)  # Output: 3.14

# 3 decimal places
print("%.3f" % number)  # Output: 3.142

# 4 decimal places
print("%.4f" % number)  # Output: 3.1416

---------------------------------------------------
Key Points:
The number after the decimal (2,3,4, etc.) determines the number of decimal places

Format pattern is always: .Nf where N is the number of decimal places

Numbers are automatically rounded to the specified decimal places

Example with your problem:

green = 12.3456789
red = 45.6789012

# 2 decimal places
print(f"{green:.2f}")  # Output: 12.35
print(f"{red:.2f}")    # Output: 45.68

# 3 decimal places
print(f"{green:.3f}")  # Output: 12.346
print(f"{red:.3f}")    # Output: 45.679

# 4 decimal places
print(f"{green:.4f}")  # Output: 12.3457
print(f"{red:.4f}")    # Output: 45.6789

"""