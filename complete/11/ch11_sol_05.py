def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input('1보다 큰 정수를 입력하세요'))
result = factorial(num)
print(num, ' 팩토리얼 : ', result ,' 입니다.')




