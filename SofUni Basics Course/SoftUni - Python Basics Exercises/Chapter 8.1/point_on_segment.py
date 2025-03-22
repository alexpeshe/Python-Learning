# Read the three integer inputs from the console
first = int(input())   # First endpoint of the segment
second = int(input())  # Second endpoint of the segment
point = int(input())   # The point we need to check

# Determine which endpoint is on the left and which is on the right
# This is important because we don't know the order of the input values
left = min(first, second)   # The leftmost endpoint (smaller x-coordinate)
right = max(first, second)  # The rightmost endpoint (larger x-coordinate)

# Calculate the distance from the point to each endpoint
distance_left = abs(left - point)   # Distance to the left endpoint
distance_right = abs(right - point)  # Distance to the right endpoint

# Find the minimum distance to either endpoint
min_distance = min(distance_left, distance_right)

# Check if the point is inside or outside the segment
# A point is inside if its x-coordinate is between the left and right endpoints (inclusive)
if left <= point <= right:
    print('in')  # Point is inside the segment
else:
    print('out')  # Point is outside the segment

# Print the minimum distance to either endpoint
print(min_distance)

# Explanations 

"""
Key Points:

Segment Orientation: The problem deals with a horizontal line segment defined by two endpoints. We don't know which endpoint is on the left or right based on the input order.

Point Location: We need to determine if a point is inside or outside the segment and find the minimum distance to either endpoint.

Inside vs Outside: A point is considered "inside" the segment if its x-coordinate is between the two endpoints (inclusive).

Distance Calculation: The distance is the absolute difference between the x-coordinates.
"""

"""
Logic Analysis:

Determining Segment Boundaries:

Using min() and max() functions ensures we correctly identify the left and right endpoints regardless of input order.

This handles cases where the segment might be given in reverse order (right to left).

Distance Calculation:

The abs() function ensures we get positive distances regardless of whether the point is to the left or right of an endpoint.

We calculate distances to both endpoints because we need to find the minimum.

Inside/Outside Check:

The condition left <= point <= right is a compact way to check if the point's x-coordinate falls within the segment boundaries.

This includes the endpoints themselves (a point exactly at an endpoint is considered "in").

Minimum Distance Logic:

If the point is inside the segment, the minimum distance will be to one of the endpoints.

If the point is outside, the minimum distance will be to the nearest endpoint.
"""

"""
Recommendations:
Add Input Validation: Consider adding checks to ensure inputs are within the specified range (-1000 to 1000).

Enhance Readability: Add more descriptive variable names or comments to make the code more self-explanatory.

Edge Case Handling: The current solution correctly handles all edge cases, including when the point is exactly at an endpoint.

Optimization: The solution is already optimal in terms of time complexity (O(1)) and space complexity (O(1)).

Alternative Approach: For educational purposes, you could also implement this using a more geometric approach, calculating the projection of the point onto the line segment.
"""