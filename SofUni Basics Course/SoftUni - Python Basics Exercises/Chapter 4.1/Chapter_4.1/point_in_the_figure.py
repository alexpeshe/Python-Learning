# Get input values
h = int(input())  # Size of each block
x = int(input())  # x-coordinate of point
y = int(input())  # y-coordinate of point

# Define boundaries for bottom rectangle (Rectangle 1)
rect1_x_min = 0
rect1_x_max = 3 * h
rect1_y_min = 0
rect1_y_max = h

# Define boundaries for top rectangle (Rectangle 2)
rect2_x_min = h
rect2_x_max = 2 * h
rect2_y_min = h
rect2_y_max = 4 * h

# Check if point is inside either rectangle (excluding borders)
inside_rect1 = (rect1_x_min < x < rect1_x_max) and (rect1_y_min < y < rect1_y_max)
inside_rect2 = (rect2_x_min < x < rect2_x_max) and (rect2_y_min < y < rect2_y_max)

# Check if point is on borders of either rectangle
border_rect1 = ((rect1_x_min <= x <= rect1_x_max) and (y == rect1_y_min or y == rect1_y_max)) or \
               ((rect1_y_min <= y <= rect1_y_max) and (x == rect1_x_min or x == rect1_x_max))

border_rect2 = ((rect2_x_min <= x <= rect2_x_max) and (y == rect2_y_min or y == rect2_y_max)) or \
               ((rect2_y_min <= y <= rect2_y_max) and (x == rect2_x_min or x == rect2_x_max))

# Determine position and print result
if inside_rect1 or inside_rect2:
    print("inside")
elif border_rect1 or border_rect2:
    print("border")
else:
    print("outside")