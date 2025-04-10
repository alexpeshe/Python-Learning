def calculate_power_iterative(base, exponent):
    """
    Calculate base raised to exponent using iterative multiplication.
    
    Args:
        base (float): The base number
        exponent (int): The power to raise the base to
        
    Returns:
        float: The result of base^exponent
    """
    # Handle special cases
    if exponent == 0:
        return 1
    
    # Initialize result to 1
    result = 1
    
    # Handle negative exponents
    is_negative = exponent < 0
    # Convert to positive for calculation
    abs_exponent = abs(exponent)
    
    # Use a while loop to multiply the base by itself 'exponent' times
    counter = 0
    while counter < abs_exponent:
        result *= base
        counter += 1
    
    # If exponent was negative, return the reciprocal
    if is_negative:
        return 1 / result
    else:
        return result

def calculate_power_recursive(base, exponent):
    """
    Calculate base raised to exponent using recursion.
    
    Args:
        base (float): The base number
        exponent (int): The power to raise the base to
        
    Returns:
        float: The result of base^exponent
    """
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        return 1 / calculate_power_recursive(base, -exponent)
    
    # Recursive case with optimization for even exponents
    if exponent % 2 == 0:
        # If exponent is even, square the result of base^(exponent/2)
        half_power = calculate_power_recursive(base, exponent // 2)
        return half_power * half_power
    else:
        # If exponent is odd, multiply base by base^(exponent-1)
        return base * calculate_power_recursive(base, exponent - 1)

def calculate_power_for_loop(base, exponent):
    """
    Calculate base raised to exponent using a for loop.
    
    Args:
        base (float): The base number
        exponent (int): The power to raise the base to
        
    Returns:
        float: The result of base^exponent
    """
    # Handle special cases
    if exponent == 0:
        return 1
    
    # Initialize result to 1
    result = 1
    
    # Handle negative exponents
    is_negative = exponent < 0
    # Convert to positive for calculation
    abs_exponent = abs(exponent)
    
    # Use a for loop to multiply the base by itself 'exponent' times
    for _ in range(abs_exponent):
        result *= base
    
    # If exponent was negative, return the reciprocal
    if is_negative:
        return 1 / result
    else:
        return result

def power_calculator():
    """
    Interactive function to calculate powers using different methods.
    """
    # Get user inputs
    try:
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the exponent (integer): "))
        
        # Dictionary to store different calculation methods
        calculation_methods = {
            "built_in": pow(base, exponent),
            "iterative": calculate_power_iterative(base, exponent),
            "recursive": calculate_power_recursive(base, exponent),
            "for_loop": calculate_power_for_loop(base, exponent)
        }
        
        # Display results from all methods
        print("\nResults using different methods:")
        print("-" * 30)
        
        # Use a for loop to iterate through the dictionary
        for method_name, result in calculation_methods.items():
            print(f"{method_name.replace('_', ' ').title()} method: {result}")
        
        # Check if all methods give the same result (within floating-point precision)
        results_list = list(calculation_methods.values())
        all_same = all(abs(result - results_list[0]) < 1e-10 for result in results_list)
        
        if all_same:
            print("\nAll methods produced the same result.")
        else:
            print("\nNote: There might be small differences due to floating-point precision.")
        
        # Additional information about the calculation
        print("\nAdditional Information:")
        print(f"- Expression: {base} ^ {exponent}")
        
        # Calculate time complexity based on exponent
        if exponent >= 0:
            print(f"- Time complexity (iterative/for-loop): O({exponent})")
            print(f"- Time complexity (recursive optimized): O(log({exponent}))")
        else:
            print(f"- Time complexity (iterative/for-loop): O({abs(exponent)})")
            print(f"- Time complexity (recursive optimized): O(log({abs(exponent)}))")
        
    except ValueError:
        print("Error: Please enter valid numbers (float for base, integer for exponent).")

# Basic implementation for compatibility with the original
number = float(input())
power = int(input())

# Using a list to store the calculation steps
steps = []
result = 1

# Alternative implementation using a for loop and list
for i in range(abs(power)):
    result *= number
    steps.append(f"Step {i+1}: {result}")

# Adjust for negative exponent
if power < 0:
    result = 1 / result
    steps.append(f"Final step (reciprocal for negative exponent): {result}")

# Print the final result to match the original output
print(result)

# Uncomment to see the step-by-step calculation
# print("\nStep-by-step calculation:")
# for step in steps:
#     print(step)

# Uncomment to run the interactive calculator
# power_calculator()


# Key Points and Explanations:

'''
Multiple Implementation Methods:

Built-in method: Uses Python's pow() function (fastest and most accurate)

Iterative method: Uses a while loop to multiply the base by itself repeatedly

Recursive method: Uses recursion with optimization for even exponents

For-loop method: Similar to iterative but uses a for loop instead

Shows different approaches to solve the same problem

Special Case Handling:

Handles exponent = 0 (returns 1)

Handles negative exponents by calculating the reciprocal

Demonstrates defensive programming techniques

Optimization Techniques:

The recursive method uses the property that x^(2n) = (x^n)^2

This reduces the time complexity from O(n) to O(log n)

Shows algorithmic optimization principles

Dictionary Usage:

Stores different calculation methods and their results

Allows for easy comparison between methods

Demonstrates dictionary iteration and value access

List Usage:

Stores step-by-step calculation results

Enables tracking the progression of the calculation

Shows how to build and display a sequence of operations

Error Handling:

Uses try-except to catch invalid inputs

Provides meaningful error messages

Shows defensive programming practices

Time Complexity Analysis:

Explains the computational efficiency of different methods

Demonstrates big O notation in practical context

Shows the importance of algorithm selection

Function Design:

Each function has a single responsibility

Includes detailed docstrings

Shows modular programming principles

Floating-Point Considerations:

Accounts for potential floating-point precision issues

Compares results with appropriate tolerance

Demonstrates awareness of numerical computing limitations

This enhanced solution not only calculates powers but provides multiple implementation methods, step-by-step tracking, and educational information about the algorithms used, making it both practical and instructional.
'''