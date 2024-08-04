import sqlite3
import turtle

# 데이터베이스 연결
conn = sqlite3.connect('test.db')

# 커서 생성
c = conn.cursor()

# 데이터 조회
c.execute('SELECT name FROM users')
users = c.fetchall()

# 터틀 설정
t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(-100, 100)

# 데이터 출력
for user in users:
    t.write(user[0], font=("Arial", 16, "normal"))
    t.right(90)
    t.forward(40)
    t.left(90)

# 터틀 종료
turtle.done()

# 연결 종료
conn.close()
