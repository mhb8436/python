admin_pw = 'admin1234!'
count = 1

while True:
    if count > 5:
        print('로그인 실패!! 횟수 초과')
        break
    
    input_pw = input('관리자 암호를 입력하세요')

    if input_pw != admin_pw:
        print('암호를 다시 확인하세요')
        count += 1
    elif input_pw == admin_pw:
        print('로그인 되었습니다')
        break


