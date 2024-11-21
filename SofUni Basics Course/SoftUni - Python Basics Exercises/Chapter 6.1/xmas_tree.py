# Prompt user to input the size of the pattern
# This determines the height and width of the pattern
n = int(input())

# Print the top border line
# ' '* (n+1): Creates leading spaces for right alignment
# '|': Adds a vertical line as a border
print(' '* (n+1) + '|')

# Main loop to create the pattern
# Iterates from row 1 to n (inclusive)
for row in range(1, n + 1):
    # Pattern creation logic for each row
    # Breakdown of print statement:
    # 1. ' ' * (n-row): Leading spaces (decreasing)
    # 2. '*'*row: Stars increasing with each row
    # 3. ' ': Space between left stars and vertical line
    # 4. '|': Vertical border line
    # 5. ' ': Space between vertical line and right stars
    # 6. '*'*row: Matching stars on right side
    print(' ' * (n-row) + '*'*row + ' ' + '|' + ' ' + '*'*row)

# Detailed Pattern Breakdown:
# For n = 5, the pattern would look like:
#      |
#     *|*
#    **|**
#   ***|***
#  ****|****
# *****|*****

# Pattern Creation Logic:
# 1. Top Border:
#    - Adds a vertical line at the top
#    - Right-aligned with leading spaces

# 2. Row Pattern:
#    - Decreasing spaces from left
#    - Increasing stars
#    - Vertical line in the middle
#    - Symmetrical star pattern on both sides

# Key Variables:
# n: Size of the pattern
# row: Current row being processed

# Mathematical Insights:
# - Total rows = n
# - Spaces decrease from n-1 to 0
# - Stars increase from 1 to n
# - Symmetrical pattern around vertical line

# Comprehensive Explanation of Pattern Mechanics:

# Space Calculation: ' ' * (n-row)
# - Controls right alignment
# - Decreases spaces as rows increase
# Example:
# Row 1: n-1 spaces
# Row 2: n-2 spaces
# ...
# Row n: 0 spaces

# Star Calculation: '*'*row
# - Increases stars with each row
# Example:
# Row 1: 1 star
# Row 2: 2 stars
# ...
# Row n: n stars

# Variations and Enhancements:
'''
def print_custom_pattern(n, left_char='*', right_char='*', border_char='|'):
    """
    Customizable pattern printing function
    
    Parameters:
    - n: Size of the pattern
    - left_char: Character for left side
    - right_char: Character for right side
    - border_char: Vertical border character
    """
    print(' '* (n+1) + border_char)
    
    for row in range(1, n + 1):
        print(
            ' ' * (n-row) +  # Leading spaces
            left_char * row +  # Left side characters
            ' ' + border_char + ' ' +  # Border with spaces
            right_char * row  # Right side characters
        )
'''

# Color Variation (using ANSI color codes)
'''
def print_colored_pattern(n):
    """
    Print pattern with color variations
    """
    # ANSI color codes
    colors = [
        '\033[91m',  # Red
        '\033[92m',  # Green
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[0m'    # Reset color
    ]
    
    print(colors[0] + ' '* (n+1) + '|' + colors[5])
    
    for row in range(1, n + 1):
        print(
            colors[row % 5] +  # Cycle through colors
            ' ' * (n-row) + '*'*row + 
            ' ' + '|' + ' ' + '*'*row + 
            colors[5]  # Reset color
        )
'''

# Potential Use Cases:
# 1. Educational tool for pattern printing
# 2. Visualization of mathematical sequences
# 3. Teaching loop and space manipulation

# Recommended Practice:
# - Experiment with different values of n
# - Try custom characters
# - Understand the mathematical pattern
# - Explore color and formatting variations

# Challenges to Consider:
# - Maintaining symmetry
# - Precise space calculations
# - Handling different input sizes

# Example function calls
# print_custom_pattern(5, '#', '@', '+')
# print_colored_pattern(5)