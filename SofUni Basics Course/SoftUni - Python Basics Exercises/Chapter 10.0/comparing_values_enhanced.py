def compare_values(type_of_comparison, values_list):
    """
    Compare values in a list based on the specified type and return the greatest value.
    
    Args:
        type_of_comparison (str): The type of comparison to perform
        values_list (list): List of values to compare
        
    Returns:
        The greatest value from the list, or the first value if all are equal
    """
    # Dictionary mapping comparison types to their corresponding conversion functions
    comparison_types = {
        "int": int,           # Convert to integer
        "float": float,       # Convert to float
        "char": ord,          # Convert to ASCII/Unicode value
        "string": str,        # Keep as string (no conversion needed)
        "len": len            # Compare by length
    }
    
    # If the type is not in our dictionary, default to string comparison
    converter = comparison_types.get(type_of_comparison, str)
    
    # Handle empty list case
    if not values_list:
        return None
    
    # Initialize with the first value
    greatest_value = values_list[0]
    converted_greatest = None
    
    try:
        # Special case for length comparison
        if type_of_comparison == "len":
            converted_greatest = len(greatest_value)
        else:
            converted_greatest = converter(greatest_value)
        
        # Use a for loop to iterate through the remaining values
        for i in range(1, len(values_list)):
            current_value = values_list[i]
            
            # Convert the current value based on the comparison type
            if type_of_comparison == "len":
                converted_current = len(current_value)
            else:
                converted_current = converter(current_value)
            
            # Compare and update the greatest value if needed
            if converted_current > converted_greatest:
                greatest_value = current_value
                converted_greatest = converted_current
                
        return greatest_value
    
    except (ValueError, TypeError) as e:
        # Handle conversion errors
        return f"Error: {e}. Cannot compare values with type '{type_of_comparison}'."

def compare_with_while_loop(type_of_comparison, values):
    """
    Alternative implementation using a while loop to find the greatest value.
    
    Args:
        type_of_comparison (str): The type of comparison to perform
        values (list): List of values to compare
        
    Returns:
        The greatest value from the list
    """
    # Dictionary of comparison functions
    comparison_functions = {
        "int": lambda x, y: int(x) > int(y),
        "char": lambda x, y: ord(x) > ord(y),
        "string": lambda x, y: x > y,
        "float": lambda x, y: float(x) > float(y),
        "len": lambda x, y: len(x) > len(y)
    }
    
    # Get the appropriate comparison function or default to string comparison
    compare = comparison_functions.get(type_of_comparison, comparison_functions["string"])
    
    if not values:
        return None
    
    # Initialize with the first value
    greatest = values[0]
    
    # Use a while loop with an index counter
    i = 1
    while i < len(values):
        # If the current value is greater, update the greatest value
        try:
            if compare(values[i], greatest):
                greatest = values[i]
        except (ValueError, TypeError):
            return f"Error: Cannot compare '{values[i]}' with type '{type_of_comparison}'."
        i += 1
        
    return greatest

def interactive_comparison():
    """
    Interactive function that allows users to compare multiple values of different types.
    """
    print("Value Comparison Tool")
    print("---------------------")
    
    # Available comparison types
    comparison_types = ["int", "float", "char", "string", "len"]
    
    print("\nAvailable comparison types:")
    for i, comp_type in enumerate(comparison_types, 1):
        print(f"{i}. {comp_type}")
    
    # Get comparison type
    while True:
        try:
            type_choice = input("\nEnter comparison type or number (1-5): ")
            
            # Check if input is a number
            if type_choice.isdigit() and 1 <= int(type_choice) <= 5:
                type_choice = comparison_types[int(type_choice) - 1]
                break
            # Check if input is a valid type
            elif type_choice in comparison_types:
                break
            else:
                print("Invalid choice. Please select a valid comparison type.")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
    
    # Get values to compare
    values = []
    print(f"\nEnter values to compare as {type_choice} (enter 'done' when finished):")
    
    while True:
        value = input("> ")
        if value.lower() == 'done':
            break
        values.append(value)
    
    if not values:
        print("No values entered.")
        return
    
    # Compare using both methods
    result1 = compare_values(type_choice, values)
    result2 = compare_with_while_loop(type_choice, values)
    
    # Display results
    print("\nResults:")
    print(f"For-loop method result: {result1}")
    print(f"While-loop method result: {result2}")
    
    # Show all values in sorted order
    try:
        if type_choice == "int":
            sorted_values = sorted(values, key=int)
        elif type_choice == "float":
            sorted_values = sorted(values, key=float)
        elif type_choice == "char":
            sorted_values = sorted(values, key=ord)
        elif type_choice == "len":
            sorted_values = sorted(values, key=len)
        else:
            sorted_values = sorted(values)
            
        print("\nAll values in sorted order:")
        for i, val in enumerate(sorted_values, 1):
            print(f"{i}. {val}")
    except (ValueError, TypeError):
        print("\nCannot sort values due to conversion errors.")

# Run the original version for compatibility
input_type = input()
value_1 = input()
value_2 = input()

# Fix the bug in the original function
def get_greater_value_fixed(i_t, v1, v2):
    """Fixed version of the original function with the bug corrected"""
    result = None

    if i_t == "int":
        if int(v1) > int(v2):
            result = v1
        elif int(v1) < int(v2):
            result = v2
        else:
            result = v1
        
    elif i_t == "char":
        if ord(v1) > ord(v2):
            result = v1
        elif ord(v1) < ord(v2):  # Fixed condition
            result = v2
        else:
            result = v2
    
    else:
        if v1 > v2:
            result = v1
        elif v1 < v2:
            result = v2
        else:
            result = v1
    
    return result

# Call the fixed function and print the result
print(get_greater_value_fixed(input_type, value_1, value_2))

# Alternative implementation using a dictionary and list
def get_greater_value_alternative(i_t, v1, v2):
    """
    Alternative implementation using a dictionary of comparison functions
    and a list to store values.
    """
    # List to store the values
    values = [v1, v2]
    
    # Dictionary mapping types to comparison functions
    comparisons = {
        "int": lambda x, y: int(x) > int(y),
        "char": lambda x, y: ord(x) > ord(y),
        # Default string comparison for any other type
        "default": lambda x, y: x > y
    }
    
    # Get the appropriate comparison function
    compare_func = comparisons.get(i_t, comparisons["default"])
    
    # Compare the values
    if compare_func(v1, v2):
        return v1
    elif compare_func(v2, v1):
        return v2
    else:
        return v1  # Return first value if equal

# Uncomment to use the alternative implementation
# print(get_greater_value_alternative(input_type, value_1, value_2))

# Uncomment to run the interactive version
# interactive_comparison()


# Key Points and Explanations:

"""
Dictionary of Functions:
--------------------------
Uses a dictionary to map comparison types to their corresponding functions

Enables dynamic selection of comparison logic based on input

Demonstrates the concept of functions as first-class objects in Python

Lambda Functions:
-------------------
Uses lambda functions for compact comparison operations

Allows for concise definition of comparison logic

Shows how to create small, anonymous functions

Error Handling:
---------------------
Implements try-except blocks to catch conversion errors

Provides meaningful error messages

Demonstrates defensive programming techniques

Multiple Implementation Approaches:
---------------------------------------
Provides both for-loop and while-loop implementations

Shows different ways to iterate through collections

Demonstrates algorithm flexibility

Interactive User Interface:
---------------------------------
Implements a user-friendly interactive mode

Allows for multiple value comparisons

Shows how to build a command-line interface

Bug Fix:
-------------------------------
Identifies and fixes the logical error in the original code

Shows the importance of code review and testing

Demonstrates debugging principles

Extended Functionality:
---------------------------------
Adds support for additional comparison types (float, length)

Allows comparison of multiple values, not just two

Shows how to extend code functionality

Sorting Demonstration:
---------------------------------
Shows how to sort values based on the comparison type

Uses the sorted() function with custom key functions

Demonstrates advanced list manipulation

Code Organization:
--------------------------------
Separates functionality into distinct functions

Uses clear naming conventions

Shows modular programming principles

This enhanced solution extends its functionality with more comparison types, multiple value support, and an interactive interface, all while demonstrating various Python programming concepts and techniques"""