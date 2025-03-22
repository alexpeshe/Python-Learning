# Core Concepts

"""
Let me explain the abs() function with simple examples:

What is abs()?
The abs() function returns the absolute value (positive value) of a number. It works with both integers and floating-point numbers.

# With positive numbers (stays the same)
print(abs(5))      # Output: 5
print(abs(10.5))   # Output: 10.5

# With negative numbers (becomes positive)
print(abs(-5))     # Output: 5
print(abs(-10.5))  # Output: 10.5

# With zero
print(abs(0))      # Output: 0

-----------------------------------------------

Common Uses

# Finding difference between numbers
num1 = 10
num2 = 25
difference = abs(num1 - num2)    # Output: 15

# Distance between points
point1 = 3
point2 = -7
distance = abs(point1 - point2)  # Output: 10

# Checking if numbers are close
tolerance = abs(actual - expected) < 0.001


 """
'''
Core Python Concepts
Data Types and Variables

Variables store data of different types (integers, floats, strings)1

Use meaningful variable names for better code readability6

Follow Python naming conventions (lowercase with underscores)6

Control Flow
'''

# If statements
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block

'''
About while and for loops 

For loop's purpose is to have specified range

Whereas While is when asking something through a condition

while n == 0: etc etc
'''

# For loops
for item in sequence(n,-1):
    # code block

for i in range(0,10):
    if i == 7:
        break
    if(i == 2):
        continue
        print(i = end='')

'''
Notes:

The key difference between if and elif:

Example one:

for i in range(0,10):
    if i == 7:           # First condition is checked independently
        break
    if i == 2:           # Second condition is checked independently
        continue
    print(i, end='')
    
Example 2:

for i in range(0,10):
    if i == 7:           # First condition is checked
        break
    elif i == 2:         # Only checked if first condition is False
        continue
    print(i, end='')

    
Key Differences:

With separate if statements:

Each condition is checked independently

Both conditions could be True (though not in this specific case)

More flexible but might be less efficient

With if-elif:

Conditions are checked in sequence

Once one condition is True, others are skipped

More efficient but more restrictive

In this specific example:

Both would actually work the same because:

When i=7, the break happens

When i=2, the continue happens

The conditions can't both be true at the same time

However, using separate if statements is more appropriate here because:

The conditions are independent of each other

We want both conditions to be checked separately

They serve different purposes (breaking vs continuing)

------------------------------------------------------------------------------------
Example where it matters:

# Using if statements
x = 10
if x > 5:    # This runs
    print("Above 5")
if x > 8:    # This also runs
    print("Above 8")
# Output: Above 5
#         Above 8

# Using if-elif
x = 10
if x > 5:    # This runs
    print("Above 5")
elif x > 8:  # This never runs because first condition was True
    print("Above 8")
# Output: Above 5

    '''


# while loops
while condition:
    # Code to execute while condition is True
    # Update variable(s) in the condition to avoid infinite loops!

#Example 1: Counting from 1 to 5


count = 1  # Initialize variable
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment to eventually exit the loop

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5

# Example 2: User Input Validation
#(Great for apps where you need to retry actions, like login attempts)

password = ""
max_attempts = 3
attempts = 0

while password != "secret123" and attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1

if password == "secret123":
    print("Access granted!")
else:
    print("Too many failed attempts. Locked!")
    
# Example 3: Data Processing
# (Sum values until a threshold is reached—useful for analytics) python

total = 0
threshold = 100

while total < threshold:
    num = float(input("Enter a number to add: "))
    total += num
    print(f"Current total: {total}")

print(f"Threshold of {threshold} reached!")

while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        break  # Terminates the loop

'''
Key Notes
Avoid Infinite Loops: Always ensure the loop’s condition will eventually become False.

Control with break/continue:

break: Exit the loop immediately.

continue: Skip to the next iteration.

When to Use while Loops
When you don’t know how many iterations you’ll need upfront (e.g., user input, reading streams of data).

For repetitive tasks until a specific state is reached (e.g., game loops, monitoring systems).
'''

# Functions and Documentation

def function_name(parameter1: type, parameter2: type) -> return_type:
    """
    Description of what the function does.

    Args:
        parameter1: Description of parameter1
        parameter2: Description of parameter2

    Returns:
        Description of return value
    """
    # function code

'''
Best Practices
Code Organization

Split large scripts into smaller, manageable functions15

Keep functions focused on single tasks8

Use built-in functions when available instead of writing custom implementations8

'''

# Error Handling and Pythonic mistakes to avoid:

try:
    # code that might raise an exception
except (ValueError, IndexError) as e:
    # handle specific exceptions

'''
Common Mistakes to Avoid
Class Variable Usage
'''

break # stops the cycle

continue 

# Incorrect
class MyClass:
    shared_list = []  # This list will be shared across all instances

# Correct
class MyClass:
    def __init__(self):
        self.instance_list = []  # Each instance gets its own list

# Variable Scope Issues

# Incorrect
x = 0
def increment():
    x += 1  # UnboundLocalError

# Correct
def increment():
    global x
    x += 1

'''
Improvement Recommendations

Practice Regularly

Set aside dedicated time for coding practice10

Work on small projects to apply concepts

Use platforms like HackerRank or LeetCode for challenges10

Code Quality

Write clear, readable code12

Add appropriate comments and documentation6

Follow PEP 8 style guidelines12

Testing

Write unit tests for your code8

Test edge cases and error conditions

Use debugging tools to find and fix issues

Learning Path
Master basic syntax and data structures14

Practice with coding exercises11

Build small projects10

Contribute to open-source projects10

Join Python communities for support and learning10

Remember to start with simple concepts and gradually move to more complex ones. Practice is key to improvement, and don't hesitate to ask questions when stuck.
'''