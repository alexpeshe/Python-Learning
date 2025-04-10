# Problem: Calculate a Number Raised to a Power
# This program takes two inputs from the user:
# 1. A number (can be decimal)
# 2. A power (integer only)
# It then calculates the result of raising the number to the given power.

# Get the base number from user (allowing decimal values)
number = float(input()) 

# Get the power/exponent from user (as an integer)
power = int(input()) 

def calculate_power(n, p):
    """
    Calculate n raised to the power of p.
    
    Args:
        n (float): The base number
        p (int): The exponent/power
        
    Returns:
        float: The result of n^p
    """
    # Use Python's built-in pow() function to calculate the power
    result = pow(n, p)
    # Return the calculated result
    return result

# Call the function with user inputs and print the result
print(calculate_power(number, power))

"""
Concepts Learned:
----------------------------------------
Function Definition: Creating a reusable function with parameters

Parameter Passing: Passing arguments to functions

Return Values: Returning calculated results from functions

Built-in Functions: Using Python's built-in pow() function

Type Conversion: Converting input to appropriate numeric types

User Input: Getting and processing user input
"""

