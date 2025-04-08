n = int(input())

"""
In Python, the backslash (\) is an escape character. When you write '/|\', the backslash is escaping the single quote that follows it, which means Python thinks your string is still continuing after that point. This makes the string unterminated.

To fix this, you need to either escape the backslash itself by using a double backslash, or use a raw string. Here are two ways to fix it:
\\"""


# First row - top of the hat
# We print dots on both sides with '/|\' in the middle
print('.' * (2*n-1) + '/|\\' + '.' * (2*n-1))

# Second row - under the top
# We print dots on both sides with '\|/' in the middle
print('.' * (2*n-1) + '\\|/' + '.' * (2*n-1))

# Third row - start of the pattern with stars
# We print dots on both sides with '***' in the middle
print('.'*(2*n-1) + '***' + '.'*(2*n-1))

# Calculate total width of the hat
width = 4 * n + 1

# Initialize variables for the dynamic part
dots_count = (width - 3) // 2  # Initial number of dots on each side
dashes = 1  # Initial number of dashes between stars

# Draw the expanding middle part of the hat
for num in range(2 * n-1):
    dots_count -= 1  # Decrease dots by 1 in each row
    dashes += 1      # Increase dashes by 1 in each row
    
    # Print the pattern: dots, star, dashes, star, dashes, star, dots
    print('.' * dots_count + '*' + '-' * dashes + '*' + '-' * dashes + '*' + '.' * dots_count)

# Bottom part - first line (solid asterisks)
print('*' * (4*n +1))

# Bottom part - second line (alternating asterisks and dots)
print('*.'* (2*n) + '*')

# Bottom part - third line (solid asterisks)
print('*' * (4*n +1))

"""
Explanation of the Solution:

Input and Dimensions:

We read an integer n that determines the size of the hat.

The total width is calculated as 4*n+1.

The total height is 2*n+5 rows.

Top Part (3 rows):

First row: Dots with /|\ in the middle

Second row: Dots with \|/ in the middle

Third row: Dots with *** in the middle

The number of dots on each side is 2*n-1 for these rows

Middle Dynamic Part (2*n-1 rows):

We start with dots_count = (width - 3) // 2 dots on each side

We start with dashes = 1 dash between stars

For each row:

Decrease dots by 1

Increase dashes by 1

The pattern is: dots + * + dashes + * + dashes + * + dots

This creates the expanding pattern of the hat

Bottom Part (3 rows):

First row: Solid line of asterisks (* repeated 4*n+1 times)

Second row: Alternating pattern of * and . (*. repeated 2*n times, plus one more *)

Third row: Another solid line of asterisks

The key to this solution is understanding how the pattern changes in each row:

The top and bottom parts are fixed in structure

The middle part follows a predictable pattern where dots decrease and dashes increase

The total width remains constant (4*n+1)

This approach creates a Christmas hat that expands from top to bottom, with decorative elements that match the requirements.
"""

'''
Key Concepts Learned from the Christmas Hat Drawing Problem

Pattern Recognition and Analysis

Identifying fixed and variable parts of a pattern

Breaking down complex visual patterns into mathematical formulas

Recognizing how elements change from row to row

String Manipulation in Python

Using string repetition with the * operator (e.g., '*' * n)

Concatenating different string patterns to form complex outputs

Building lines with precise character positioning

Escape Characters

Understanding that \ is an escape character in Python strings

Properly escaping backslashes using double backslashes (\\)

Recognizing and fixing syntax errors related to escape sequences

Dynamic Pattern Generation

Calculating initial values based on input parameters

Systematically modifying values in each iteration (decreasing dots, increasing dashes)

Maintaining consistent overall width while changing internal elements

Loop Control and Iteration

Using loops to generate repetitive but changing patterns

Calculating the exact number of iterations needed (2*n-1 for the middle part)

Updating multiple variables within each iteration

Mathematical Relationships

Deriving formulas for element counts (width = 4*n+1)

Calculating symmetrical elements (dots on both sides)

Ensuring patterns align correctly through precise calculations

Code Structure and Organization

Breaking the drawing into logical sections (top, middle, bottom)

Initializing variables before loops

Using clear, consistent naming conventions

Problem Decomposition

Breaking a complex drawing into simpler components

Handling each section of the drawing with appropriate logic

Ensuring all parts connect seamlessly
'''

# AI solution
'''
n = int(input())

# Calculate total width
width = 4 * n + 1

# First row - top of the hat
dots_count = (width - 3) // 2
print('.' * dots_count + '/|\\' + '.' * dots_count)

# Second row
print('.' * dots_count + '\\|/' + '.' * dots_count)

# Middle part of the hat (dynamic part)
dots_count -= 1
dashes = 1

# First row of the middle part
print('.' * dots_count + '*' + '-' * dashes + '*' + '-' * dashes + '*' + '.' * dots_count)

# Rest of the middle part
for i in range(2 * n - 1):
    dots_count -= 1
    dashes += 1
    print('.' * dots_count + '*' + '-' * dashes + '*' + '-' * dashes + '*' + '.' * dots_count)

# Bottom part of the hat
print('*' * width)
print('*.' * (width // 2) + '*' * (width % 2))
print('*' * width)

'''
