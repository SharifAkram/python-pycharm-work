import turtle

turtle.bgcolor("black")
turtle.pensize(2)

def curve():
    for i in range(200):
        turtle.right(1)  # curve of heart
        turtle.forward(1)

turtle.speed(0)
turtle.color("red", "pink")

turtle.begin_fill()  # heart will be filled with color
turtle.left(140)
turtle.forward(111.65)
curve() # runs code inside curve function

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
