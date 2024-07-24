n = int(input('양의 정수를 입력하세요'))

if n > 0:
    print('number', n)
    if n % 2 == 0:
        print('number 는 짝수')
    else:
        print('number 는 홀수')
else:
    print('number는 양수가 아니다.')


