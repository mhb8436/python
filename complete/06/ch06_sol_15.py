import turtle

# 사용자로부터 색상과 도형 종류 입력 받기
color = input("원하는 색상을 입력하세요 (red, green, blue): ")
shape = input("그리고 싶은 도형을 입력하세요 (circle, square, triangle): ")

# 터틀 설정
screen = turtle.Screen()
screen.title("터틀 도형 그리기")
pen = turtle.Turtle()
pen.speed(2)  # 터틀 속도 설정

# 중첩 조건문을 사용하여 색상과 도형 결정
if color in ["red", "green", "blue"]:
    pen.color(color)
    if shape == "circle":
        pen.begin_fill()
        pen.circle(50)
        pen.end_fill()
    elif shape == "square":
        pen.begin_fill()
        pen.forward(100)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)
        pen.end_fill()
    elif shape == "triangle":
        pen.begin_fill()
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
        pen.end_fill()
    else:
        print("올바른 도형을 입력하지 않았습니다.")
else:
    print("올바른 색상을 입력하지 않았습니다.")

# 프로그램 종료 대기
turtle.done()




