# Read the x and y coordinates of the point from user input
x = int(input())   
y = int(input())   

# Check if the point is inside the first rectangle
# A point is inside a rectangle if its x coordinate is between the left and right edges
# AND its y coordinate is between the bottom and top edges
pointInRect1 = 2 <= x <= 12 and -3 <= y <= 1

# Check if the point is inside the second rectangle
pointInRect2 = 4 <= x <= 10 and -5 <= y <= 3

# If the point is inside either rectangle, it's considered inside the figure
if pointInRect1 or pointInRect2:
    print("in")
else:
    print('out')


"""

Comprehensive Analysis
Logic Breakdown:
Input Handling: The program reads two integers representing the x and y coordinates of a point.

Rectangle Checks:

For Rectangle 1: We check if x is between 2 and 12 (inclusive) AND if y is between -3 and 1 (inclusive).

For Rectangle 2: We check if x is between 4 and 10 (inclusive) AND if y is between -5 and 3 (inclusive).

Figure Determination:

If the point is inside EITHER rectangle, it's considered inside the figure.

Otherwise, it's outside the figure.

Output: The program prints "in" if the point is inside the figure, and "out" otherwise.

"""

"""
Visual Representation:
Based on the code, the figure would look something like this:
"""
'''
    2      4      10     12
    |      |      |      |
  3 +------+------+------+
    |      |      |      |
    |      |Rectangle 2  |
    |      |      |      |
  1 +------+------+------+
    |                    |
    |    Rectangle 1     |
    |                    |
 -3 +------+------+------+
    |      |      |      |
    |      |      |      |
 -5 +------+------+------+
'''

'''Key Points:

Boundary Inclusion: The solution considers points exactly on the boundaries to be inside the rectangles (using <= and >= rather than < and >).

Logical OR Operation: A point is considered inside the figure if it's inside either of the two rectangles.

Coordinate System: The problem uses a standard Cartesian coordinate system where positive y is up and positive x is right.
'''

'''Recommendations

Improved Clarity: Add comments to explain the dimensions and positions of the rectangles.

Function-Based Approach: Consider refactoring the code into functions for better readability:'''

"""
def is_point_in_rectangle(x, y, x_min, x_max, y_min, y_max):
    return x_min <= x <= x_max and y_min <= y <= y_max

def is_point_in_figure(x, y):
    return (is_point_in_rectangle(x, y, 2, 12, -3, 1) or 
            is_point_in_rectangle(x, y, 4, 10, -5, 3))
"""

'''
Input Validation: Add validation to ensure inputs are within the specified range (-1000 to 1000).

Visual Feedback: For educational purposes, consider adding a simple visualization of the figure and the point's position.

Edge Case Handling: The current solution correctly handles edge cases (points on boundaries), but it's good to explicitly document this behavior.

This solution efficiently solves the problem with O(1) time complexity, making it optimal for the given constraints.
'''
