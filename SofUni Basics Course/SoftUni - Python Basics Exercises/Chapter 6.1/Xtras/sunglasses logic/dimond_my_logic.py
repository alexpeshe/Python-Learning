# Get the input from the user and convert it to an integer
n = int(input())

# Initialize variables
my_range = 0  # This will determine how many rows to print
stars = 1     # Start with one star for the top row
if_n_even = n % 2 == 0  # Check if n is even
dash = (n - stars) // 2  # Calculate the number of dashes on each side

# Determine the range and number of stars based on whether n is even or odd
if if_n_even:
    my_range = n - 1  # For even n, we need one less row for the upper half
    stars = 2         # Start with two stars for the top row
else:
    my_range = n      # For odd n, we use n directly

# Print the top row of the diamond
print('-' * int(dash) + '*' * stars + '-' * int(dash))

# Adjust my_range to determine how many rows to print in the lower half
if my_range % 2 == 0:
    my_range -= n + 1  # If my_range is even, adjust it
else:
    my_range -= n + 1  # If my_range is odd, adjust it

# Print the upper half of the diamond (excluding the top row)
for row in range(0, int(my_range)):
    # Print each row with a star on each end and dashes in the middle
    print('*' + '_' * (dash + 1) + '*')

# Print the middle part of the diamond
for row in range(0, int(my_range - 4)):
    # Print rows with dashes and stars
    print('-' + '*' + '-' * dash + '*' + '-')

# Print the middle row of the diamond
print('*' + '-' * (n - 2) + '*')

# Print the lower part of the diamond
for row in range(0, int(my_range - 4)):
    # Print rows with dashes and stars
    print('-' + '*' + '-' * dash + '*' + '-')

# Print the bottom row of the diamond
print('-' * int(dash) + '*' * stars + '-' * int(dash))
