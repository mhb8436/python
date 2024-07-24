import turtle

screen = turtle.Screen()
shape = screen.textinput('도형선택', 
    """그리고 싶은 도형을 입력하세요 
    ( triangle, square, circle) -> """)

t = turtle.Turtle()

if shape == "triangle":
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
elif shape == 'square':
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
elif shape == 'circle':
    t.circle(100)
else:
    t.write('알수업는 도형입니다.')

turtle.exitonclick()
