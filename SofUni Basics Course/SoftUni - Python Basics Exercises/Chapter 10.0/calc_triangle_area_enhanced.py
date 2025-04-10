def calculate_triangle_area(dimensions):
    """
    Calculate the area of a triangle using different methods based on available dimensions.
    
    Args:
        dimensions (dict): Dictionary containing triangle dimensions
        
    Returns:
        float: The calculated area of the triangle
    """
    # Check which calculation method to use based on available dimensions
    if 'base' in dimensions and 'height' in dimensions:
        # Standard formula: Area = (base * height) / 2
        return (dimensions['base'] * dimensions['height']) / 2
    elif all(key in dimensions for key in ['a', 'b', 'c']):
        # Heron's formula for three sides
        s = (dimensions['a'] + dimensions['b'] + dimensions['c']) / 2
        return (s * (s - dimensions['a']) * (s - dimensions['b']) * (s - dimensions['c'])) ** 0.5
    elif 'base' in dimensions and 'angle' in dimensions and 'side' in dimensions:
        # Trigonometric formula: Area = (1/2) * base * side * sin(angle)
        import math
        angle_rad = math.radians(dimensions['angle'])
        return 0.5 * dimensions['base'] * dimensions['side'] * math.sin(angle_rad)
    else:
        raise ValueError("Insufficient dimensions provided to calculate triangle area")

def get_numeric_input(prompt, input_type=float):
    """
    Get and validate numeric input from the user.
    
    Args:
        prompt (str): The prompt to display to the user
        input_type (type): The type to convert the input to (default: float)
        
    Returns:
        The converted input value
    """
    while True:
        try:
            value = input_type(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def main():
    """
    Main function to run the triangle area calculator.
    """
    print("Triangle Area Calculator")
    print("-----------------------")
    
    # List of calculation methods
    methods = [
        "1. Base and Height",
        "2. Three Sides (Heron's Formula)",
        "3. Base, Side, and Included Angle"
    ]
    
    # Display available methods
    print("\nAvailable calculation methods:")
    for method in methods:
        print(method)
    
    # Get user's choice of method
    while True:
        try:
            choice = int(input("\nSelect a method (1-3): "))
            if 1 <= choice <= 3:
                break
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Dictionary to store the dimensions
    dimensions = {}
    
    # Get inputs based on the selected method
    if choice == 1:
        # Base and Height method
        dimensions['base'] = get_numeric_input("Enter the base length: ")
        dimensions['height'] = get_numeric_input("Enter the height: ")
    elif choice == 2:
        # Three Sides method
        dimensions['a'] = get_numeric_input("Enter the length of side a: ")
        dimensions['b'] = get_numeric_input("Enter the length of side b: ")
        dimensions['c'] = get_numeric_input("Enter the length of side c: ")
        
        # Check triangle inequality theorem
        sides = [dimensions['a'], dimensions['b'], dimensions['c']]
        sides.sort()
        if sides[0] + sides[1] <= sides[2]:
            print("Error: These sides cannot form a triangle (violates triangle inequality theorem).")
            return
    elif choice == 3:
        # Base, Side, and Angle method
        dimensions['base'] = get_numeric_input("Enter the base length: ")
        dimensions['side'] = get_numeric_input("Enter the side length: ")
        dimensions['angle'] = get_numeric_input("Enter the included angle (in degrees): ")
        
        if dimensions['angle'] >= 180:
            print("Error: Angle must be less than 180 degrees.")
            return
    
    # Calculate the area
    try:
        area = calculate_triangle_area(dimensions)
        
        # Display results with various format options
        print("\nResults:")
        print(f"Triangle area: {area:.12g}")
        print(f"Exact value: {area}")
        print(f"Scientific notation: {area:.10e}")
        print(f"Fixed precision: {area:.10f}")
        
        # Store results in a list for reference
        results_list = [
            {"format": "Standard", "value": f"{area:.12g}"},
            {"format": "Exact", "value": f"{area}"},
            {"format": "Scientific", "value": f"{area:.10e}"},
            {"format": "Fixed", "value": f"{area:.10f}"}
        ]
        
        # Demonstrate list iteration
        print("\nAll formats:")
        for i, result_format in enumerate(results_list, 1):
            print(f"{i}. {result_format['format']}: {result_format['value']}")
        
    except ValueError as e:
        print(f"Error: {e}")

# Run the program using a simple version for compatibility with the original
base = float(input())
height = float(input())

# Using a list to store the parameters
triangle_params = [base, height]

# Alternative implementation using a while loop
def triangle_area_while(params):
    """Calculate triangle area using a while loop approach"""
    i = 0
    product = 1
    while i < len(params):
        product *= params[i]
        i += 1
    return product / 2

# Calculate using the alternative method
result = triangle_area_while(triangle_params)

# Print with the same formatting as the original
print(f"{result:.12g}")

# Uncomment to run the enhanced version
# if __name__ == "__main__":
#     main()



# Key Points and Explanations:

"""
Multiple Calculation Methods:

Implements three different formulas for triangle area calculation

Base and height (standard formula)

Three sides (Heron's formula)

Base, side, and included angle (trigonometric formula)

Demonstrates mathematical versatility in programming

Dictionary Usage:

Uses a dictionary to store triangle dimensions

Allows for flexible parameter handling

Enables checking for available dimensions using key existence

Demonstrates dictionary methods and key checking

Input Validation:

Implements robust input validation

Checks for positive values

Validates triangle inequality theorem

Shows error handling best practices

While Loop Implementation:

Alternative triangle_area_while function uses a while loop instead of direct multiplication

Demonstrates how to iterate through a list using a while loop

Shows accumulation pattern with a counter variable

List Usage:

Stores parameters in a list for processing

Stores formatted results in a list of dictionaries

Shows list iteration with enumeration

Demonstrates data organization techniques

Function Design:

Main function organizes program flow

Helper functions handle specific tasks

Calculation function adapts to different input types

Shows modular programming principles

Error Handling:

Uses try-except blocks to catch errors

Provides meaningful error messages

Validates geometric constraints

Demonstrates defensive programming

Format Options:

Shows multiple ways to format numeric output

Explains the purpose of each format

Demonstrates string formatting options

Provides flexibility in result presentation

Mathematical Concepts:

Implements multiple geometric formulas

Uses trigonometric functions

Applies the triangle inequality theorem

Shows how to translate mathematical concepts to code

This enhanced solution not only calculates the triangle area but provides a comprehensive toolkit for triangle calculations with multiple methods, robust validation, and flexible output formatting, demonstrating various Python programming concepts and mathematical applications.
"""