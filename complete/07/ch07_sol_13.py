height = 10

for i in range(height):
    # 공백 출력
    print(height - i - 1)
    for j in range(height - i - 1):
        print(" ", end="")
    # 별 출력
    for k in range(2 * i + 1):
        print("*", end="")
    print()  # 각 행이 끝날 때 줄 바꿈



