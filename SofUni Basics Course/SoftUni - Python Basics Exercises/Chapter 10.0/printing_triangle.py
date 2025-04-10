# Problem: Print a Triangle of Numbers
# This program prints a triangle pattern of numbers based on user input.
# The pattern consists of two parts:
# 1. Increasing rows (from 1 to n)
# 2. Decreasing rows (from n-1 to 1)

# Get user input for the triangle height
n = int(input())

def printing_triangle(num):
    # Part 1: Print increasing rows (1 to num)
    for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
        # For each row i, print numbers from 1 to i
        for j in range(1, i + 1):  # Inner loop to print each number in the current row
            print(f"{j} ", end="")  # Print number followed by space, stay on same line
        print()  # Move to the next line after completing each row
    
    # Part 2: Print decreasing rows (num-1 to 1)
    for k in range(num-1, 0, -1):  # Loop from num-1 down to 1
        # For each row k, print numbers from 1 to k
        for l in range(1, k + 1):  # Inner loop to print each number in the current row
            print(f"{l} ", end="")  # Print number followed by space, stay on same line
        print()  # Move to the next line after completing each row

# Call the function with user input
printing_triangle(n)

"""
Concepts Learned:
----------------------------------------------------------------------------------

Nested Loops: Using outer loops to control rows and inner loops to control columns

Function Definition: Creating reusable code with parameters

Range Function: Using range() with different parameters to control iteration

String Formatting: Using f-strings to format output

Print Function: Using the end parameter to control line breaks

"""

# Alternative Solution Using Different Approaches:

"""
def print_triangle_alternative(height):
    

    '''Alternative implementation of triangle printing using:
    - List comprehensions
    - String joining
    - Dictionary for pattern storage
    - While loop for the second part'''

    # Dictionary to store pattern templates
    patterns = {
        "increasing": "Printing increasing rows (1 to {}):",
        "decreasing": "Printing decreasing rows ({} to 1):"
    }
    
    print(patterns["increasing"].format(height))
    
    # Part 1: Increasing rows using list comprehension and join
    i = 1
    while i <= height:
        # Create a list of strings and join them with spaces
        row = ' '.join([str(j) for j in range(1, i + 1)])
        print(row)
        i += 1
    
    print(patterns["decreasing"].format(height-1))
    
    # Part 2: Decreasing rows using a for loop and list
    for i in range(height-1, 0, -1):
        # Create an empty list to store the numbers
        row_numbers = []
        
        # Append each number to the list
        for j in range(1, i + 1):
            row_numbers.append(str(j))
        
        # Join the list elements and print
        print(' '.join(row_numbers))

# Get user input
try:
    height = int(input("Enter triangle height: "))
    if height <= 0:
        print("Please enter a positive integer.")
    else:
        print_triangle_alternative(height)
except ValueError:
    print("Invalid input. Please enter a number.")
"""

# Key Points and Explanations:

'''

Dictionary Usage:
------------------
Stores template strings for pattern descriptions

Makes the code more maintainable by centralizing messages

Demonstrates how to format strings from dictionary values.


List Comprehension:
---------------------

[str(j) for j in range(1, i + 1)] creates a list of strings in one line

More concise than traditional for loops for creating lists

Converts numbers to strings as part of the comprehension


String Joining:
-------------------

' '.join(list_of_strings) joins list elements with spaces

More efficient than concatenating strings in a loop

Creates the entire row at once rather than printing each number separately


While Loop vs. For Loop:
-------------------------

While loop used for the first part to demonstrate an alternative to for loops

For loop used in the second part, showing both approaches

Shows how the same task can be accomplished with different loop types


Error Handling:
-------------------

Try-except block catches invalid inputs

Input validation ensures positive height values

Makes the program more robust against user errors


Different Approaches to Same Problem:
--------------------------------------

First part uses list comprehension and join

Second part builds a list manually then joins it

Demonstrates multiple ways to achieve the same result


Code Organization:
-----------------------

Function docstring explains purpose and implementation details

Logical separation between different parts of the triangle

Clear variable names that indicate their purpose

--------------------------------------------------------------------------
This alternative implementation demonstrates more advanced Python concepts while achieving the same output as the original code, showing how the same problem can be solved in multiple ways'''