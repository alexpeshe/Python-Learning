import turtle  # Import the turtle graphics module

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the shape of the turtle to "turtle"
my_turtle.shape("turtle")

# Loop to draw three triangles
for i in range(0, 3):  # Repeat the following block 3 times
    my_turtle.left(30)  # Turn the turtle left by 30 degrees
    my_turtle.forward(200)  # Move the turtle forward by 200 units (length of the triangle side)
    my_turtle.left(120)  # Turn the turtle left by 120 degrees to form the first angle of the triangle
    my_turtle.forward(200)  # Move the turtle forward by another 200 units
    my_turtle.left(120)  # Turn the turtle left by 120 degrees to form the second angle of the triangle
    my_turtle.forward(200)  # Move the turtle forward by another 200 units to complete the triangle

# Finish the turtle graphics drawing
turtle.done()  # This line keeps the turtle graphics window open until it is closed by the user

#TODO (P.S. Don't forget to add some turns to that turtle code! 🐢) like left, right etc

'''
Additional notes 

Turtle graphics in Python offers several movement and turning commands. Here are the main ones:

Forward and Backward:

forward(distance) or fd(distance): Move forward
backward(distance) or bk(distance): Move backward
Turning:

right(angle) or rt(angle): Turn right by specified angle
left(angle) or lt(angle): Turn left by specified angle
Precise Turning:

setheading(angle) or seth(angle): Set the orientation of the turtle to a specific angle
Circular Movement:

circle(radius, extent=None, steps=None): Draw a circle or part of a circle
Going to Specific Coordinates:

goto(x, y): Move to a specific x, y coordinate
setx(x): Set the turtle's x coordinate
sety(y): Set the turtle's y coordinate
Home:

home(): Move the turtle to the origin (0, 0) and set heading to 0
Pen Control:

penup() or pu(): Lift the pen (move without drawing)
pendown() or pd(): Lower the pen (draw while moving)
Advanced Movements:

dot(size=None, color=None): Draw a dot
stamp(): Leave an impression of the turtle shape at the current location
These commands give you a wide range of options for creating various shapes and patterns. You can combine them in different ways to create complex drawings. For example, you could use circle() to create curved shapes, or goto() to jump to different parts of your drawing canvas.'''