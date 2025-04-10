# Problem: Determine if a number is positive, negative, or zero

# Get user input as an integer
number = int(input())

"""
Parameters in Python functions serve several crucial purposes and understanding them is key to writing effective code. 
Let's examine why parameters are needed and how to identify them using your example function.

-----------------------------------------------------------------
"""
# Define a function to check the sign of a number
def sign_int(num):
    # Check if the number is zero
    if num == 0:
        print(f"The number {num} is zero")
    # Check if the number is positive
    elif num > 0:
        print(f"The number {num} is positive")
    # If not zero or positive, the number must be negative
    else:
        print(f"The number {num} is negative")

# Call the function with the user input
sign_int(number)

"""
Concepts learned:

User input and type conversion

Function definition

Conditional statements (if-elif-else)

String formatting (f-strings)
"""

# Alternative solution using a while loop and dictionary

"""
This alternative solution demonstrates more advanced concepts such as error handling, data structures (dictionary and list), and loop usage. 
It also provides a more flexible approach by allowing multiple inputs and using a dictionary for message storage.
"""

'''
# Dictionary to store number types and their corresponding messages
number_types = {
    "zero": "The number {num} is zero",
    "positive": "The number {num} is positive",
    "negative": "The number {num} is negative"
}

# Initialize an empty list to store user inputs
numbers = []

# Use a while loop to get multiple inputs from the user
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if user_input.lower() == 'q':
        break
    
    # Try to convert the input to an integer
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Process the list of numbers
for num in numbers:
    # Determine the number type
    if num == 0:
        num_type = "zero"
    elif num > 0:
        num_type = "positive"
    else:
        num_type = "negative"
    
    # Print the result using the dictionary
    print(number_types[num_type].format(num=num))
'''

"""
ey points and explanations:

Dictionary usage:

We use a dictionary number_types to store the messages for each number type.

This allows for easy message retrieval and maintenance.

While loop for input:

The while loop allows the user to enter multiple numbers.

The loop continues until the user enters 'q' to quit.

Error handling:

We use a try-except block to handle potential ValueError when converting input to an integer.

List for storing inputs:

We store all valid inputs in a list numbers for later processing.

For loop for processing:

We use a for loop to iterate through the list of numbers and process each one.

Dictionary key access:

We use the determined number type as a key to access the appropriate message from the dictionary.

String formatting:

We use the format() method to insert the number into the message string.
"""