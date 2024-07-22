import turtle

# 스크린 설정
screen = turtle.Screen()
screen.title("연산자 예제")
screen.bgcolor("white")

# 터틀 설정
t = turtle.Turtle()
t.speed(1)
t.pensize(3)

# 덧셈 예제
t.penup()
t.goto(-200, 100)
t.pendown()
t.write("덧셈: 3 + 2 = " + str(3 + 2), font=("Arial", 16, "normal"))

# 뺄셈 예제
t.penup()
t.goto(-200, 50)
t.pendown()
t.write("뺄셈: 5 - 3 = " + str(5 - 3), font=("Arial", 16, "normal"))

# 곱셈 예제
t.penup()
t.goto(-200, 0)
t.pendown()
t.write("곱셈: 4 * 2 = " + str(4 * 2), font=("Arial", 16, "normal"))

# 나눗셈 예제
t.penup()
t.goto(-200, -50)
t.pendown()
t.write("나눗셈: 8 / 2 = " + str(8 / 2), font=("Arial", 16, "normal"))

# 터틀 숨기기
t.hideturtle()

# 스크린 유지
screen.mainloop()
