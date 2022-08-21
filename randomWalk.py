import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
turtle.shape("circle")
turtle.speed(10)
turtle.pensize(5)
turtle.hideturtle()

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

directions = [0, 90, 180, 270]

for i in range(200):
    turtle.color(randomColor())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

