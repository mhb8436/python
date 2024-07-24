num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))
operation = input("원하는 연산을 선택하세요 (+, -, *, /): ")

if operation == "+":
    print(f"결과: {num1 + num2}")
elif operation == "-":
    print(f"결과: {num1 - num2}")
elif operation == "*":
    print(f"결과: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"결과: {num1 / num2}")
    else:
        print("0으로 나눌 수 없습니다.")
else:
    print("올바른 연산을 선택하세요.")


