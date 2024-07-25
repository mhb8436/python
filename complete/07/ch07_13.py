currentTemp = 32.2
targetTemp  = float(input('에어컨 설정온도 : '))

for i in range(100):
    currentTemp -= 0.1
    print('현재온도 =>', format(currentTemp, '.2f'))
    if currentTemp <= targetTemp:
        break

print('냉방 종료')


