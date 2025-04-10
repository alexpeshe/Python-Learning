# Problem: Print a Pattern with Dashes and Slashes
# This program prints a pattern that consists of:
# 1. A top border of dashes
# 2. A body with dashes and slash patterns
# 3. A bottom border of dashes

# Get user's input for the pattern size
n = int(input())

def print_dashes(num):
    """
    Function to print a line of dashes.
    The length of the line is 2 times the input number.
    
    Args:
        num: The size parameter that determines the length of the dash line
    """
    print("-" * (num * 2))  # String multiplication to repeat the dash character

def print_body(number):
    """
    Function to print the body of the pattern.
    The body consists of lines with a dash at each end and slash patterns in between.
    
    Args:
        number: The size parameter that determines the pattern structure
    """
    for i in range(1, number - 1):  # Loop from 1 to number-2 (creates number-2 rows)
        # Each line has:
        # - A dash at the beginning
        # - A series of "\\/" patterns (number-1 times)
        # - A dash at the end
        print("-" + "\\/" * int((2 * number - 2) / 2) + "-")
        # Note: (2*number-2)/2 simplifies to (number-1), making this equivalent to:
        # print("-" + "\\/" * (number-1) + "-")


# Print the complete pattern
print_dashes(n)  # Top border
print_body(n)    # Pattern body
print_dashes(n)  # Bottom border


# Alternative solution commented out in the original code
'''
print_dashes(n)
for i in range(1, n-1):
    print_body(n)
print_dashes(n)
'''
# Note: This alternative solution has a logical error as it would call print_body(n) 
# multiple times, which would print multiple complete bodies, not individual lines.

'''
Concepts Learned:
---------------------------------------------------------
String Multiplication: Using * operator to repeat strings

Functions: Creating reusable code blocks with parameters

Loops: Using for loops to repeat operations

Expression Evaluation: Calculating values for string repetition

Pattern Printing: Building complex patterns from simple components'''