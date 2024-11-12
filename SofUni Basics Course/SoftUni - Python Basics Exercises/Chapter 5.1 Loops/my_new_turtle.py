import turtle  # Import the turtle graphics module

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the shape of the turtle to "turtle"
my_turtle.shape("turtle")

# Loop to draw three triangles
for i in range(0, 4):  # Repeat the following block 3 times
    my_turtle.left(30)  # Turn the turtle left by 30 degrees
    my_turtle.forward(200)  # Move the turtle forward by 200 units (length of the triangle side)
    my_turtle.left(120)  # Turn the turtle left by 120 degrees to form the first angle of the triangle
    my_turtle.forward(200)  # Move the turtle forward by another 200 units
    my_turtle.left(120)  # Turn the turtle left by 120 degrees to form the second angle of the triangle
    my_turtle.forward(200)  # Move the turtle forward by another 200 units to complete the triangle

    my_turtle.left(-30) # Turn the turtle right by 30 degrees (using negative left turn)
    my_turtle.penup() # Lift the pen up (turtle will move without drawing)
    my_turtle.backward(50) # Move backward 50 units without drawing
    my_turtle.pendown() # Put the pen down (turtle will draw when moving)
    my_turtle.backward(100) # Move backward 100 units while drawing
    my_turtle.penup() # Lift the pen up again
    my_turtle.forward(150) # Move forward 150 units without drawing
    my_turtle.pendown() # Put the pen down again
    my_turtle.left(30) # Turn the turtle left by 30 degrees

# Finish the turtle graphics drawing
turtle.done()  # This line keeps the turtle graphics window open until it is closed by the user