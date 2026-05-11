import turtle 

screen = turtle.Screen()
screen.screensize(200, 200)
screen.bgcolor("orange")

polygon = turtle.Turtle()

num_sides = 6
side_length = 50
angle = 360 / num_sides 

for a in range (num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
