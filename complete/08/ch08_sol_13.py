import turtle

pen = turtle.Turtle()
pen.speed(5)
colors = ["red","blue","green","yellow","purple","orange"]

for i in range(len(colors)):
    pen.color(colors[i])
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.forward(150)
    pen.pendown()

turtle.exitonclick()


