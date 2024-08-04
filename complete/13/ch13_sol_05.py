print('메모장 프로그램 입니다.')

while True:
    memo = input('메모를 입력하세요')
    if memo == "exit":
        break
    elif memo == "read":
        with open('../memo.txt','r') as file:
            print(f"메모내용 => {file.read()}")
    else:
        with open('../memo.txt', 'a') as file:
            file.write(memo)
        
            



