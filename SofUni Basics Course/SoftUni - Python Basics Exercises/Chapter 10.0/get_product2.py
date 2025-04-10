'''
num1 = float(input())
num2 = float(input())
result = None
'''

# Function Definition: Creates a function that calculates the product of two numbers
def get_product(num_1, num_2):
    # Local variable: Stores the result of multiplication
    result = num_1 * num_2
    # Return statement: Sends the calculated value back to the caller
    return result

# For loop: Iterates from 1 to 10 (range(1, 11) excludes the upper bound)
for i in range(1, 11):
    # Function call inside a loop: Calls get_product with the same value for both parameters
    # Print statement: Displays the result of each function call
    print(get_product(i, i))  # This prints i² for each value of i from 1 to 10


"""
Key Concepts Learned:
Function Definition and Usage:

Functions encapsulate reusable code

Parameters allow functions to work with different inputs

Return statements pass calculated values back to the caller

Loops:

For loops iterate through a sequence (like range())

While loops continue until a condition is no longer true

Both can be used to repeat operations with different values

Data Structures:

Lists store ordered collections of items

Dictionaries store key-value pairs for efficient lookups

Both can be created and populated in loops

Functional Programming Concepts:

List comprehensions provide concise ways to create lists

Dictionary comprehensions create dictionaries efficiently

Map function applies a function to all items in an iterable

Variable Scope:

Local variables (like 'result') exist only within their function

Loop variables (like 'i') are accessible within their loop scope

Code Organization:

Breaking code into functions improves readability and reusability

Different implementations can achieve the same result with varying approaches

Comments explain the purpose and functionality of code sections"""


# Alternative Implementation with a While Loop:

"""
# Function remains the same
def get_product(num_1, num_2):
    result = num_1 * num_2
    return result

# Initialize counter for while loop
i = 1
# While loop that continues until i reaches 11
while i <= 10:
    # Call the function and print the result
    print(get_product(i, i))
    # Increment counter to avoid infinite loop
    i += 1
""" 

# Alternative Implementation with Lists:

'''
def get_product(num_1, num_2):
    result = num_1 * num_2
    return result

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Method 1: Using a for loop with the list
for num in numbers:
    print(get_product(num, num))

# Method 2: Using list comprehension to store all results
results = [get_product(num, num) for num in numbers]
print("All results:", results)

# Method 3: Using map function
squared_values = list(map(lambda x: get_product(x, x), numbers))
print("Squared values:", squared_values)
'''

# Alternative Implementation with Dictionary:

"""
def get_product(num_1, num_2):
    result = num_1 * num_2
    return result

# Create a dictionary with numbers as keys and their squares as values
squares_dict = {}
for i in range(1, 11):
    squares_dict[i] = get_product(i, i)

# Print each key-value pair
for number, square in squares_dict.items():
    print(f"The square of {number} is {square}")

# Alternative dictionary creation using dictionary comprehension
squares_dict_comp = {num: get_product(num, num) for num in range(1, 11)}
print("Dictionary of squares:", squares_dict_comp)
"""

