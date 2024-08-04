members = {}
flag = True

while flag:
    num = int(input("1. 회원가입, 2. 회원목록, 3. 프로그램 종료"))

    if num == 1:
        id = input('아이디를 입력하세요  =>')
        pw = input('비밀번호를 입력하세요 =>')
        members[id] = pw
    
    elif num == 2:
        print('-' * 30)
        print("아이디 : 비밀번호")
        print('-' * 30)
        for key in members:
            print(key, '\t:\t', members[key])
        print('-' * 30)
    elif num == 3:
        print('프로그램을 종료합니다')
        flag = False


