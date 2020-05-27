import turtle

def pentagram(x=100):
    scr = turtle.Screen()
    for _ in range(5):
        turtle.right(144)
        turtle.forward(x)
    turtle.exitonclick()

def square(x):
    scr = turtle.Screen()
    for _ in range(4):
        turtle.forward(x)
        turtle.right(90)
    turtle.exitonclick()

def triangle(x,y=120):
    scr = turtle.Screen()
    for _ in range(3):
        turtle.forward(x)
        turtle.left(y)
    turtle.exitonclick()

def circle(x=1):
    scr = turtle.Screen()
    turtle.circle(x)
    turtle.exitonclick()

