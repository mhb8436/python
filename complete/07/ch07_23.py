import random

number_to_guess = random.randint(1, 100)
attempts = 0
guessed = False

print("숫자 맞추기 게임에 오신 것을 환영합니다!")
print("1부터 100 사이의 숫자를 맞춰보세요.")

while not guessed:
    user_guess = int(input("숫자를 입력하세요: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("더 높은 숫자입니다. 다시 시도하세요.")
    elif user_guess > number_to_guess:
        print("더 낮은 숫자입니다. 다시 시도하세요.")
    else:
        guessed = True
        print(f"축하합니다! 숫자를 맞췄습니다. 맞춘 숫자: {number_to_guess}")
        print(f"총 시도 횟수: {attempts}")


