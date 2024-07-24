import turtle
sc = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')

side_length = sc.textinput('길이', '한변의 길이를 입력하세요')
side_length = int(side_length)
color = 'blue' if side_length > 100 else 'red'
t.color(color)

t.forward(side_length)
t.right(90)
t.forward(side_length)
t.right(90)
t.forward(side_length)
t.right(90)
t.forward(side_length)

turtle.exitonclick()


