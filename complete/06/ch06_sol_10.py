import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')

color = screen.textinput('색성 선택', 
    '색상을 입력하세요(빨강색, 녹색, 파랑색, 검정색)')

if color == '빨강색':
    t.pencolor('red')
elif color == '녹색':
    t.pencolor('green')
elif color == '파랑색':
    t.pencolor('blue')
elif color == '검정색':
    t.pencolor('black')

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
