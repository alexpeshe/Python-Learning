import turtle  # Import the turtle graphics module

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the shape of the turtle to "turtle"
my_turtle.shape("turtle")

# Set the turtle color to orange
my_turtle.color('navy')

# Prepare to move without drawing
my_turtle.penup()
# Move to the center of the screen (0, 0)
my_turtle.goto(0, 200)
# Put the pen down to start drawing
my_turtle.pendown()

for i in range(3):

    # Initial length
    length = 200

    # Amount to increase by each time
    decrease = 5

    for i in range(22):
        my_turtle.left (30)
        my_turtle.forward (length)
        my_turtle.left (120)
        my_turtle.forward (length)
        my_turtle.left (120)
        my_turtle.forward(length)
    
        length -= decrease  # Increase the length of the line

# Keep the window open until manually closed
turtle.done()