import turtle

t = turtle.Turtle()
t.shape('turtle')

def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.right(120)

def draw_circle():
    t.circle(100)

def draw_shapes():
    draw_square()
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    draw_triangle()
    t.penup()
    t.goto(300, 0)
    t.pendown()
    draw_circle()

draw_shapes()

turtle.exitonclick()




    