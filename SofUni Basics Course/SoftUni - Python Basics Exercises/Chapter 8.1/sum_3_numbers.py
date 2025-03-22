# This program reads three integers and checks if any two of them add up to the third.
# If such a relationship exists, it outputs the equation in the format "smaller + larger = sum".
# If no such relationship exists, it outputs "No".

# Read three integers from user input
a = int(input())   # Read the first number
b = int(input())   # Read the second number
c = int(input())   # Read the third number

# Check if a + b = c
if a+b == c:
    # If true, determine which of a or b is larger
    if a>b:
        # If a is larger, print with b (smaller) first
        print('%d + %d = %d' % (b, a, c))
    else:
        # If b is larger or they're equal, print with a first
        print('%d + %d = %d' % (a, b, c))

# Check if a + c = b
elif a+c == b:
    # If true, determine which of a or c is larger
    if a>c:
        # If a is larger, print with c (smaller) first
        print('%d + %d = %d' % (c, a, b))
    else:
        # If c is larger or they're equal, print with a first
        print('%d + %d = %d' % (a, c, b))

# Check if b + c = a
elif b+c == a:
    # If true, determine which of b or c is larger
    if b>c:
        # If b is larger, print with c (smaller) first
        print('%d + %d = %d' % (c, b, a))
    else:
        # If c is larger or they're equal, print with b first
        print('%d + %d = %d' % (b, c, a))

# If none of the above conditions are met
else:
    # No valid addition equation exists among the three numbers
    print('No')


    """
    Also:
    
The %d is a format specifier used in C-style string formatting in Python. It serves the following purposes:

Placeholder: It acts as a placeholder in a string where an integer value will be inserted.

Integer representation: The d in %d stands for "decimal integer". It indicates that the corresponding value should be formatted as a signed integer in decimal (base 10) representation.

Value substitution: When used with the % operator, it allows for dynamic insertion of integer values into a string."""