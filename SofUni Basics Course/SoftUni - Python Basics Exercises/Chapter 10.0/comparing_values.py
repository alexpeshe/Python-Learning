# Problem: Compare Two Values and Return the Greater One
# This program compares two values based on their type (integer, character, or string)
# and returns the greater value. If the values are equal, it returns one of them.

# Get the type of comparison to perform
input_type = input()  # Expected values: "int", "char", or any other string for string comparison

# Get the two values to compare
value_1 = input()
value_2 = input()

def get_greater_value(i_t, v1, v2):
    """
    Compare two values based on the specified type and return the greater one.
    
    Args:
        i_t (str): The type of comparison to perform ("int", "char", or any other string for string comparison)
        v1 (str): The first value to compare
        v2 (str): The second value to compare
        
    Returns:
        str: The greater value as a string, or one of the values if they are equal
    """
    result = None  # Initialize result variable

    if i_t == "int":
        # Integer comparison
        if int(v1) > int(v2):
            result = v1  # First value is greater
        elif int(v1) < int(v2):
            result = v2  # Second value is greater
        else:
            result = v1  # Values are equal, return the first one
        
    elif i_t == "char":
        # Character comparison using ASCII/Unicode values
        if ord(v1) > ord(v2):
            result = v1  # First character has higher ASCII/Unicode value
        elif ord(v1) < ord(v2):  # Note: This condition has a logical error (should be ord(v1) < ord(v2))
            result = v2  # Second character has higher ASCII/Unicode value
        else:
            result = v2  # Characters are equal, return the second one
    
    else:
        # String comparison (lexicographical order)
        if v1 > v2:
            result = v1  # First string is greater lexicographically
        elif v1 < v2:
            result = v2  # Second string is greater lexicographically
        else:
            result = v1  # Strings are equal, return the first one
    
    return result  # Return the determined result

# Call the function with the user inputs and print the result
print(get_greater_value(input_type, value_1, value_2))

# Concepts Learned:

'''
Conditional Logic: Using if-elif-else statements for decision making

Type-Based Comparison: Handling different types of comparisons based on input

Type Conversion: Converting strings to integers for numeric comparison

Character Encoding: Using ord() to get the ASCII/Unicode value of characters

String Comparison: Comparing strings lexicographically

Function Parameters: Passing and using multiple parameters

Return Values: Returning results from functions
'''
        
