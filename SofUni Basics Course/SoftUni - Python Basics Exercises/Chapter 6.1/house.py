# Read the input size of the house
n = int(input())

# Initialize variables for the house pattern
my_range = 0    # Number of rows for the roof part
stars = 1       # Initial number of stars in the first row
dash = (n-stars)/2  # Calculate initial number of dashes on each side

# Check if the input number is even 
if_n_even = n%2==0

# Determine the number of rows for the roof based on whether n is even or odd
if if_n_even:
    # For even numbers:
    my_range = n//2     # Roof will be half the total height
    stars = 2           # Start with 2 stars for even-numbered houses
else:
    # For odd numbers:
    my_range = n//2 + 1 # Roof will be slightly more than half the height
    # stars remains 1 for odd-numbered houses

# Create the roof of the house
for row in range(0, int(my_range)):
    # Print each row of the roof:
    # 1. Dashes on the left side
    # 2. Stars in the middle
    # 3. Dashes on the right side
    print('-'*int(dash) + '*'*stars + '-'*int(dash))
    
    # Increase the number of stars for the next row
    stars += 2
    
    # Recalculate the number of dashes to maintain symmetry
    dash = (n - stars)//2

# Calculate the number of rows for the base of the house
other_rows = n - my_range

# Create the base of the house
for row in range(0, other_rows):
    # Print each row of the base:
    # 1. Left wall '|'
    # 2. Stars filling the width (n-2)
    # 3. Right wall '|'
    print('|' + '*'*(n-2) +'|')

'''
Detailed Explanation:
Input and Initial Setup

Takes an input n which determines the size of the house
Initializes variables for creating the house pattern
Handling Even and Odd Sizes

Checks if n is even or odd
Adjusts the roof pattern accordingly:
For even numbers: roof is exactly half the height
For odd numbers: roof is slightly more than half the height
Roof Creation

Uses a loop to create the roof part of the house
Starts with few stars and increases gradually
Maintains symmetry by adjusting dashes on both sides
Each iteration adds 2 more stars
Base Creation

Creates the remaining rows as the base of the house
Uses walls ('|') and fills the inside with stars
Example Outputs:
For n = 5:

Insert Code
Edit
Copy code
--*--
-***-
*****
|***|
|***|
For n = 4:

Insert Code
Edit
Copy code
-**-
****
|**|
|**|
Key Characteristics:
Symmetrical pattern
Roof grows from center
Base maintains consistent width
Adapts to both even and odd input sizes
The code creates a house-like pattern where the roof expands from the center and the base maintains a consistent width, with the overall shape determined by the input number.
'''

     