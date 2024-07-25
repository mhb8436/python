import turtle

screen = turtle.Screen()

sides = screen.textinput('다각형', '면의 개수 입력')
sides = int(sides)
length = 100

angle = 360 / sides  # 각 내부 각도 계산
for _ in range(sides):
    turtle.forward(length)
    turtle.left(angle)

# 터틀 설정
turtle.speed(2)  # 터틀 속도 조절
turtle.color("blue")  # 펜 색상 설정

# 마우스를 클릭하면 창을 닫음
turtle.exitonclick()

