import turtle
t = turtle.Turtle()
t.shape('turtle')

side_length = int(input('한변길이를 입력하세요'))
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


