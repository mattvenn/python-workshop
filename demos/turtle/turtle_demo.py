import turtle                   # Allows us to use turtles
wn = turtle.Screen()            # Creates a playground for turtles
my_turtle = turtle.Turtle()     # Create a turtle, assign to my_turtle
my_turtle.shape('turtle')       # make it look like a turtle

my_turtle.forward(50)           # Tell my_turtle to move forward by 50 units
my_turtle.left(90)              # Tell my_turtle to turn by 90 degrees
my_turtle.color("blue")         # change the colour
my_turtle.forward(30)           # Complete the second side of a rectangle
my_turtle.penup()               # lift the pen
my_turtle.forward(30)
my_turtle.pendown()             # lower the pen
my_turtle.pensize(5)            # increase pen size
my_turtle.forward(30)

turtle.mainloop()               # wait
