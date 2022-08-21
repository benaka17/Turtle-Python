import turtle as t
import random

turtle = t.Turtle()
turtle.speed("fastest")
t.colormode(255)
turtle.hideturtle()

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

for i in range(1000):
    turtle.color(randomColor())
    turtle.circle(100)
    turtle.color(randomColor())
    heading = turtle.heading()
    turtle.setheading(heading + 2)

screen = t.Screen()
screen.exitonclick()

