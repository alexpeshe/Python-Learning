import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

for i in range(3):  # Loop to create 3 sides of the triangle
    my_turtle.forward(200)  # Move forward by 200 units
    my_turtle.right(120)  # Turn right by 120 degrees

turtle.exitonclick()
turtle.mainloop()