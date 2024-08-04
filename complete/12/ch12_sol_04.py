import turtle
import random
t = turtle.Turtle()
t.shape('turtle')

def random_color():
    colors = ['red','blue','green','orange','purple','pink','yellow']
    return random.choice(colors)

def draw_random_shape():
    shape_type = random.choice(['circle','square','triangle'])
    size = random.randint(100,200)
    color = random_color()
    t.color(color)
    if shape_type == 'circle':
        t.circle(size)
    elif shape_type == 'sqaure':
        for _ in range(4):
            t.forward(size)
            t.right(90)
    elif shape_type == 'triangle':
        for _ in range(3):
            t.forward(size)
            t.right(120)

def move_randomly():
    angle = random.randint(0, 360)
    distance = random.randint(50, 200)
    t.penup()
    t.right(angle)
    t.forward(distance)
    t.pendown()


for _ in range(10):
    draw_random_shape()
    move_randomly()


turtle.exitonclick()
