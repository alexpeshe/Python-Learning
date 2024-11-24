# Read the input size for the butterfly pattern
n = int(input())

# Calculate the size of the wing (excluding the body)
# Subtract 2 to create space for the body and middle section
half_row_size = n - 2

# Draw the upper wing of the butterfly
for i in range(half_row_size):
    # Alternate between '*' and '-' for visual texture
    if i % 2 == 0:  # Even rows (0, 2, 4...)
        # Create left side with asterisks
        left_part = '*' * half_row_size
        # Create middle section with wing-like slashes
        middle_part = r'\ /'  # Raw string to handle backslash
        # Create right side with asterisks matching left side
        right_part = '*' * half_row_size
    else:           # Odd rows (1, 3, 5...)
        # Create left side with dashes
        left_part = '-' * half_row_size
        # Keep the same middle section
        middle_part = r'\ /'
        # Create right side with dashes
        right_part = '-' * half_row_size
    
    # Print the complete row combining left, middle, and right parts
    print(left_part + middle_part + right_part)

# Draw the body of the butterfly
# Center the '@' symbol with equal spaces on both sides
print(' ' * (n - 1) + '@' + ' ' * (n - 1))

# Draw the lower wing of the butterfly
for i in range(half_row_size):
    # Similar pattern to upper wing, but with reversed slashes
    if i % 2 == 0:  # Even rows (0, 2, 4...)
        # Create left side with asterisks
        left_part = '*' * half_row_size
        # Create middle section with inverted wing-like slashes
        middle_part = '/ \\'
        # Create right side with asterisks
        right_part = '*' * half_row_size
    else:           # Odd rows (1, 3, 5...)
        # Create left side with dashes
        left_part = '-' * half_row_size
        # Keep the same middle section
        middle_part = '/ \\'
        # Create right side with dashes
        right_part = '-' * half_row_size
    
    # Print the complete row combining left, middle, and right parts
    print(left_part + middle_part + right_part)