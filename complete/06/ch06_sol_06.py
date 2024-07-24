endCarNum = int(input('차량번호 끝자리 입력:'))

if endCarNum == 1 or endCarNum == 6:
    print('월요일에 주차 가능합니다.')
elif endCarNum == 2 or endCarNum == 7:
    print('화요일에 주차 가능합니다.')
elif endCarNum == 3 or endCarNum == 8:
    print('수요일에 주차 가능합니다.')
elif endCarNum == 4 or endCarNum == 9:
    print('목요일에 주차 가능합니다.')            
else:
    print('금요일에 주차 가능합니다.')   



    
