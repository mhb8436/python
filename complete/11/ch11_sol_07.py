import turtle
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

# 로깅 데코레이터 정의
def log_event(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing: {func.__name__} 
                     with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Finished: {func.__name__}")
        return result
    return wrapper

# 터틀 객체 생성
screen = turtle.Screen()
screen.title("Turtle Graphics with Logging")
my_turtle = turtle.Turtle()

# 데코레이터를 적용한 터틀 함수 정의
@log_event
def move_forward(t, distance):
    t.forward(distance)

@log_event
def turn_right(t, angle):
    t.right(angle)

@log_event
def turn_left(t, angle):
    t.left(angle)

@log_event
def move_backward(t, distance):
    t.backward(distance)

# 함수 실행
def main():
    moves = [
        (move_forward, 100),
        (turn_right, 90),
        (move_forward, 100),
        (turn_right, 90),
        (move_forward, 100),
        (turn_right, 90),
        (move_forward, 100)
    ]
    
    for move, value in moves:
        move(my_turtle, value)
    
    # 화면 클릭 시 종료
    screen.exitonclick()

if __name__ == "__main__":
    main()
