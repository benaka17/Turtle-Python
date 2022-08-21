from turtle import Turtle, Screen

turtle = Turtle()

def drawShape(numSides):
    angle = 360 / numSides
    for i in range(numSides):
        turtle.forward(50)
        turtle.right(angle)

for i in range(3,9):
    drawShape(i)

# Has to be at the bottom
screen = Screen()
screen.exitonclick()