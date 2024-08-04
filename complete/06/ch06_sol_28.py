a1 = int(input('전자계산기일반'))
a2 = int(input('패키지활용'))
a3 = int(input('PC운영체제'))
a4 = int(input('정보통신일반'))

avg = ( a1 + a2 + a3 + a4 ) /4 
if avg > 60:
    if a1 < 40 or a2 < 40 or a3 < 40 or a4 < 40:
        print('불합격')
    else:
        print('합격')
else:
    print('불합격')

