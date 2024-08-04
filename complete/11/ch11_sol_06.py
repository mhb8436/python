import turtle

t = turtle.Turtle()
t.shape('turtle')

def draw_line(t, length):
    if length > 0:
        t.forward(length)
        t.right(90)
        draw_line(t, length - 10)


t.penup()
t.goto(-100,0)
t.pencolor('blue')
t.pendown()

draw_line(t, 100)

turtle.exitonclick()


