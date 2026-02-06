import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

pen.penup()
pen.goto(0, -100)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(0, 30)
pen.setheading(0)
pen.down()

pen.fillcolor("yellow")
pen.begin_fill()

for _ in range(5):
    pen.forward(80)
    pen.right(144)

pen.end_fill()

turtle.done()