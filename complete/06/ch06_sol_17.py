import random

dice = random.randint(1, 6)
print(f"주사위 눈: {dice}")

if dice == 1:
    print("아쉽네요! 다음에 더 좋은 운을 기원합니다.")
elif dice == 6:
    print("축하합니다! 최고점입니다.")
else:
    print("괜찮은 점수네요!")


