import turtle  # Import the turtle graphics module

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the shape of the turtle to "turtle"
my_turtle.shape("turtle")

# Set the turtle color to green
my_turtle.color("green")

# Move to the starting position
my_turtle.penup()
my_turtle.goto(0, 200)  # Starting at the top point
my_turtle.pendown()

# Draw the pentagram
for i in range(5):
    my_turtle.forward(250)  # Draw a line
    my_turtle.right(144)     # Turn 144 degrees to the right (or use left(144))

# Finish the turtle graphics drawing
turtle.done()  # This line keeps the turtle graphics window open until it is closed by the user

''' 
alternative solution 
import turtle

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the shape of the turtle to "turtle"
my_turtle.shape("turtle")

# Set the turtle color to green
my_turtle.color("green")

# Set the starting position to the center (0, 0)
# No need for penup() and goto() here, as (0, 0) is the default starting position

my_turtle.penup()
my_turtle.goto(0,200)
my_turtle.pendown()

# Calculate the length of each side
side_length = 200

# Move forward by half the side length to start the star from its center
my_turtle.forward(side_length / 2)


# Draw the pentagram
for i in range(5):
    my_turtle.forward(side_length)
    my_turtle.right(144)  # or left(144)

# Finish the turtle graphics drawing
turtle.done()'''