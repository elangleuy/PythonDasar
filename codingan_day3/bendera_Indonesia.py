import turtle

t = turtle.Turtle()
t.speed(0)

# Merah
t.penup()
t.goto(-200, 0)
t.pendown()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

# Putih
t.penup()
t.goto(-200, -100)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

turtle.done()
