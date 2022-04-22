import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

t = Turtle()
t.width(20)
t.speed(0)
t.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw():
    x = -230
    y = 210
    t.penup()
    t.setpos(x, y)

    for _ in range(10):
        for _ in range(10):
            t.color(random_color())
            t.pendown()
            t.forward(1)
            t.penup()
            t.forward(50)
        y -= 50
        t.setpos(x, y)


draw()


screen = Screen()
screen.exitonclick()