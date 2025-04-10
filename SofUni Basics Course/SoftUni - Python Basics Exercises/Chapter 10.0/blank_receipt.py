def print_header():
    print("CASH RECEIPT\n-------------------------") # this is the symbol for a new line \n

def print_body():
    print("Charged to______________________\nReceived by______________________")

def print_footer():
    print("--------------------------------\n @ SoftUni")

def print_receipt():
    print_header()
    print_body()
    print_footer()
    
    # return print_body, print_header, print_footer

print_receipt()

"""
Yes, the key takeaways from this exercise are:

Function Definition vs. Function Execution:

When you define a function using def function_name():, you're creating the function

When you write function_name() with parentheses, you're executing the function

When you write just function_name without parentheses, you're referencing the function object but not running it

Function Composition:

You can create a main function that calls other functions

This promotes modular code organization and reusability

Function Return Values:

Functions can return values that can be used by other functions

If you don't explicitly return anything, the function returns None by default

Function Hierarchy:

You can organize code by creating a hierarchy of functions

This makes your code more maintainable and easier to understand

Code Organization:

Breaking functionality into separate functions makes your code more readable

Each function should ideally have a single responsibility

Function Calls:

The parentheses () are what trigger the function to execute

This is a fundamental syntax element in Python and many other programming languages

These concepts are foundational to functional programming and good software design in general.

"""