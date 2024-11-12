import turtle

# Setup the turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color('orange')
my_turtle.speed(0)  # Fastest speed

# Move to starting position
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

# Starting length and increment
length = 10
increment = 5

# Draw 22 spiral iterations
for _ in range(22):
    # Draw first triangle (top)
    for _ in range(3):
        my_turtle.forward(length)
        my_turtle.left(120)
    
    # Position for second triangle (bottom right)
    my_turtle.left(120)
    
    # Draw second triangle
    for _ in range(3):
        my_turtle.forward(length)
        my_turtle.left(120)
    
    # Position for third triangle (bottom left)
    my_turtle.left(120)
    
    # Draw third triangle
    for _ in range(3):
        my_turtle.forward(length)
        my_turtle.left(120)
    
    # Prepare for next iteration
    my_turtle.left(120)  # Return to starting orientation
    my_turtle.left(5)    # Small rotation for spiral effect
    length += increment  # Increase size for next iteration

turtle.done()