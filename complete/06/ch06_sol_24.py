print('1:월~금, 2:토/일, 3:공휴일')
dayofWeek = int(input('요일을 선택하세요'))
carType = int(input('차종을 선택하세요.(1:버스, 2:승용차) '))

if dayofWeek == 1:
    print('버스 전용차로 단속 중')
    if carType != 1:
        print('버스전용차로 위반!!')
    else:
        print('버스')
else:
    print('토요일,일요일, 공휴일은 단속하지 않음')


