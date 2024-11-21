# Read the input size of the sunglasses
n = int(input())

# Calculate the number of stars on each side
# 2*n creates the width of stars on each side of the sunglasses
stars = 2*n

# Calculate the number of spaces in the middle
# 5*n - 4*n simplifies to n (creates the space between the two lens frames)
space = 5*n - 4*n

# Calculate the number of slashes in the lens frame
# 2*n-2 creates the number of slashes for the lens frame
slash = 2*n-2

# Check if n is even (used for special handling of middle row)
n_even = n%2==0

# Print the top row of stars
# '*'*stars creates stars on left side
# ' '*space creates space in middle
# '*'*stars creates stars on right side
print('*'*stars + ' '*space + '*'*stars)

# Iterate through the middle rows of the sunglasses
# range(1, (n-2)+1) creates rows from 1 to number of middle rows
for row in range(1, (n-2)+1):
    # Special condition for middle row of odd-sized sunglasses
    # Checks if current row is middle row and n is odd
    if row == n//2 and not n_even:
        # Print row with vertical bars (|) in the middle
        print('*' + '/'*slash + '*' + '|'*space + '*'  + '/'*slash + '*')
    
    # Special condition for middle row of even-sized sunglasses
    # Checks if current row is just before middle and n is even
    elif n_even and row == (n//2)-1:
        # Print row with vertical bars (|) in the middle
        print('*' + '/'*slash + '*' + '|'*space + '*'  + '/'*slash + '*')
    
    # For all other rows
    else:
        # Print rows with spaces in the middle
        print('*' + '/'*slash + '*' + ' '*space + '*'  + '/'*slash + '*')

# Print the bottom row of stars (same as top row)
print('*'*stars + ' '*space + '*'*stars)

'''
Key points in the code:

Calculates the number of stars, spaces, and slashes based on input size n
Handles both odd and even sized sunglasses differently
Prints top and bottom rows with full stars
Handles middle rows with special conditions:
For odd-sized sunglasses: vertical bars at exact middle
For even-sized sunglasses: vertical bars at row just before middle
Other rows have spaces in the middle
The code creates a sunglasses pattern that adapts to different sizes while maintaining the characteristic look with lens frames and optional middle vertical bars.

Example outputs:

For n = 3: Odd-sized, vertical bars in exact middle
For n = 4: Even-sized, vertical bars one row before middle
'''


'''
Alternative solution
n = int(input())

stars = 2*n
space = n
slash = 2*n-2

# Top row
print('*'*stars + ' '*space + '*'*stars)

# Middle rows
for row in range(1, n-1):
    if row == n//2:
        # Row with vertical bars
        print('*' + '/'*slash + '*' + '|'*space + '*' + '/'*slash + '*')
    else:
        # Other rows
        print('*' + '/'*slash + '*' + ' '*space + '*' + '/'*slash + '*')

# Bottom row
print('*'*stars + ' '*space + '*'*stars)
'''
