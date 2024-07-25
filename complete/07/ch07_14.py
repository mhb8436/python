currentTemp = 32.2
targetTemp  = float(input('에어컨 설정온도 : '))

while currentTemp >= targetTemp:
    currentTemp -= 0.1
    print('현재온도 => ', format(currentTemp, '.2f'))

print('냉방 종료')



