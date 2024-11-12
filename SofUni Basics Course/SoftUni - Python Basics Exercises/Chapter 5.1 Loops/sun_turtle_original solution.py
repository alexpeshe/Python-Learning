import turtle  # Import the turtle graphics module

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the shape of the turtle to "turtle"
my_turtle.shape("turtle")

# Set the turtle color to orange
my_turtle.color('orange')

# Prepare to move without drawing
my_turtle.penup()
# Move to the center of the screen (0, 0)
my_turtle.goto(0, 0)
# Put the pen down to start drawing
my_turtle.pendown()

# Loop 36 times to create a full circular pattern
for i in range(36):
    my_turtle.forward(250)  # Draw a line outward
    my_turtle.right(10)     # Turn 10 degrees clockwise
    my_turtle.backward(250) # Draw a line back to the center
    my_turtle.right(10)     # Turn another 10 degrees clockwise

# Keep the window open until manually closed
turtle.done()
