import turtle

screen = turtle.Screen()
screen.title("Square Window") 
screen.setup(width=500, height=500)
screen.bgcolor("lavender")

square = turtle.Turtle()
square.color("purple")

square.penup()
square.goto(0, 200) 
square.write("Square", align="center", font=("Arial", 24, "bold"))

square.goto(-50, 50)
square.pendown()

num_sides = 4
side_length = 100
angle = 360 / num_sides

for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)

turtle.done()


