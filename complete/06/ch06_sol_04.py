h = int(input('키를 입력하세요(cm)'))
w = int(input('몸무게를 입력하세요(kg)'))

h = h/100
b = w/(h**2)

if b >= 0 and b < 18.5:
    print('저체중', b)
elif b >= 18.5 and b < 23:
    print('정상', b)
elif b >= 23 and b < 25:
    print('비만전단계', b)
elif b >= 25:
    print('비만', b)



