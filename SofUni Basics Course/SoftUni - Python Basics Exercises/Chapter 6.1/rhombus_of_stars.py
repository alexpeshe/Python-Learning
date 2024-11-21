# Prompt the user to input the size of the pyramid
# This will determine the height and width of the pattern
n = int(input())

# Upper half of the pyramid
# Loop from row 1 to n (inclusive)
for row in range(1, n + 1):
    # Print spaces before stars to create the triangular shape
    # (n-row) calculates the number of spaces needed
    # This creates a right-aligned triangular pattern
    # '* '* row prints the stars, with number of stars increasing each row
    print(' ' * (n-row) + '* '* row)

# Lower half of the pyramid
# Loop from row 1 to n-1 (exclusive)
for row in range(1, n):
    # Print spaces at the beginning, increasing with each row
    # '* ' * (n-row) prints decreasing number of stars
    # This creates the bottom half of the pyramid
    print(' ' * row + '* ' * (n-row))

# Detailed breakdown of the pattern creation:

# Upper Half Logic:
# row = 1: "    *"        (4 spaces, 1 star)
# row = 2: "   * *"       (3 spaces, 2 stars)
# row = 3: "  * * *"      (2 spaces, 3 stars)
# row = 4: " * * * *"     (1 space, 4 stars)
# row = 5: "* * * * *"    (0 spaces, 5 stars)

# Lower Half Logic:
# row = 1: " * * * *"     (1 space, 4 stars)
# row = 2: "  * * *"      (2 spaces, 3 stars)
# row = 3: "   * *"       (3 spaces, 2 stars)
# row = 4: "    *"        (4 spaces, 1 star)

# Example output for n = 5:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# Below is the single for loop solution 

'''
Logic: 
- Loop from row 1 to n (inclusive)
- For each row, print spaces before stars to create the triangular shape
- The number of spaces decreases with each row, and the number of stars increases
- The stars are printed with a space between each star


Key Concepts Explained:

Two-Part Pattern
First loop creates the upper half of the pyramid
Second loop creates the lower half of the pyramid
Space Calculation
' ' * (n-row) dynamically calculates spaces
Decreases from left to right in upper half
Increases from left to right in lower half
Star Multiplication
'* '* row creates stars
Number of stars increases in upper half
Number of stars decreases in lower half
Loop Ranges
Upper half: range(1, n + 1)
Starts at 1
Goes up to and including n
Lower half: range(1, n)
Starts at 1
Goes up to, but not including n
Pattern Symmetry
Creates a symmetrical diamond-like shape
Controlled by precise space and star calculations
Variations to Try:

Change n to see how the pattern scales
Experiment with different characters instead of '*'
Would you like me to elaborate on any part of the explanation?'''


