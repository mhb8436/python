import turtle
t = turtle.Turtle()
t.shape('turtle')

angle = int(input('회전각도를 입력하세요'))
length = int(input('전진길이를 입력하세요'))

t.forward(length)
t.right(angle)
t.forward(length)
t.right(angle)
t.forward(length)

turtle.exitonclick()



