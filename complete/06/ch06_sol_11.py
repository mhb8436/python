import turtle

# 스크린 설정
screen = turtle.Screen()
screen.title("if 문 예제")
screen.bgcolor("white")

# 터틀 설정
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

# 사용자 입력 받기
number = screen.numinput("숫자 입력", "양수, 음수 또는 0을 입력하세요:")

# if 문 예제
if number > 0:
    t.color("green")
    t.write("양수입니다!", font=("Arial", 16, "normal"))
    t.forward(100)
elif number < 0:
    t.color("red")
    t.write("음수입니다!", font=("Arial", 16, "normal"))
    t.backward(100)
else:
    t.color("blue")
    t.write("0입니다!", font=("Arial", 16, "normal"))
    t.right(90)
    t.circle(100)

# 터틀 숨기기
t.hideturtle()

# 스크린 유지
screen.mainloop()
