# for i in range(1, 101):
#     if '3' in str(i) or '6' in str(i) or '9' in str(i):
#         print(i, '짝!')
#     else:
#         print(i)



for num in range(1, 101):
    if num <= 9:
        if num % 3 == 0:
            print(num, '짝!', end='')
        else:
            print(num, end='')
    else:
        print(num, end='')
        firstNum = num // 10
        secondNum = num % 10
        if firstNum % 3 == 0:
            print('짝!', end='')
        if secondNum % 3 == 0 and secondNum != 0:
            print('짝!', end='')
    print()


    