from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.back(10)

def left():
    new_angle = t.heading() + 5
    t.setheading(new_angle)

def right():
    t.right(5)

def clear():
    screen.resetscreen()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")


screen.exitonclick()