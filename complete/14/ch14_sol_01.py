import threading
import time
import random

# 전역 변수를 이용하여 타이머와 게임 상태를 관리합니다
game_over = False
user_guess = -1

# 타이머 함수
def countdown_timer(duration):
    global game_over
    for i in range(duration, 0, -1):
        if game_over:
            return
        print(f"남은 시간: {i}초", end='\r')
        time.sleep(1)
    game_over = True
    print("\n시간이 초과되었습니다! 게임 종료.")

# 숫자 추측 함수
def guess_number(target):
    global user_guess, game_over
    while not game_over:
        try:
            user_input = input("숫자를 맞춰보세요: ")
            user_guess = int(user_input)
            if user_guess == target:
                print("정답입니다! 게임을 종료합니다.")
                game_over = True
                return
            elif user_guess < target:
                print("더 큰 숫자입니다.")
            else:
                print("더 작은 숫자입니다.")
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

# 메인 프로그램
if __name__ == "__main__":
    # 랜덤 숫자 생성
    target_number = random.randint(1, 100)
    duration = 30  # 타이머 설정 (초)

    # 쓰레드 생성
    timer_thread = threading.Thread(
        target=countdown_timer, args=(duration,))
    guess_thread = threading.Thread(
        target=guess_number, args=(target_number,))

    # 쓰레드 시작
    timer_thread.start()
    guess_thread.start()

    # 모든 쓰레드가 종료될 때까지 대기
    guess_thread.join()
    timer_thread.join()

    if user_guess == target_number:
        print("축하합니다! 숫자를 맞추셨습니다.")
    else:
        print(f"아쉽습니다. 정답은 {target_number}였습니다.")


