import math  # Import the math module for using mathematical functions

# Get input from the user to determine the size of the diamond
n = int(input())  # n determines the number of rows in the upper half of the diamond

# Print the top border of the diamond
print('%'*2*n)  # Print '%' 2n times to create the top border

num_rows = n  # Initialize num_rows with n

# Adjust num_rows if n is even to ensure symmetry
if n % 2 == 0:
    num_rows -= 1  # Decrease num_rows by 1 if n is even

# Loop to print the body of the diamond
for i in range(0, num_rows):
    print('%', end=' ')  # Print '%' at the start of each row, with a space after

    # Check if we're at the middle row of the diamond
    if i == math.floor(num_rows/2):
        # Print the middle row with '**' in the center
        print((' '*(n-2)) + '**' + (' '*(n-2)) + '%')
    else:
        # Print empty spaces for non-middle rows
        print(' ' * (n*2-2))

    print('%', end=' ')  # Print '%' at the end of each row, with a space before

# Print the bottom border of the diamond
print('%'*2*n)  # Print '%' 2n times to create the bottom border
