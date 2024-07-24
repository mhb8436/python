import random

target = random.randint(1, 10)
guess = int(input("1에서 10 사이의 숫자를 맞춰보세요: "))

if guess == target:
    print("정답입니다!")
else:
    print(f"틀렸습니다. 정답은 {target}입니다.")
