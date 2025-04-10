# Problem: Calculate the Area of a Triangle
# This program calculates the area of a triangle using the formula: Area = (base * height) / 2

# Get user input for the base and height of the triangle
# Convert the inputs to floating-point numbers to handle decimal values
base = float(input())    # Base length of the triangle
height = float(input())  # Height of the triangle

def triangle_area(b, h):
    """
    Calculate the area of a triangle given its base and height.
    
    Args:
        b (float): The base length of the triangle
        h (float): The height of the triangle
        
    Returns:
        float: The calculated area of the triangle
    """
    area = (b * h) / 2   # Formula for triangle area: (base * height) / 2
    return area          # Return the calculated value

# Call the function with the user inputs and store the result
result = triangle_area(base, height)

# Print the result with formatting
# The :.12g format specifier ensures:
# - Up to 12 significant digits are displayed
# - Trailing zeros are removed
# - Scientific notation is used for very large or small numbers
print(f"{result:.12g}")


"""
Concepts Learned:
--------------------------------------------
Function Definition: Creating a reusable function with parameters

Parameter Passing: Passing arguments to functions

Return Values: Returning calculated results from functions

Mathematical Operations: Using arithmetic operations in Python

Type Conversion: Converting string input to floating-point numbers

String Formatting: Using f-strings with format specifiers

Precision Control: Controlling the display of floating-point numbers
"""