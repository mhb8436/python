# 연락처 딕셔너리
contacts = {}

# 메인 프로그램
while True:
    print("\n1. 연락처 추가")
    print("2. 연락처 조회")
    print("3. 연락처 삭제")
    print("4. 모든 연락처 출력")
    print("5. 종료")
    
    choice = input("원하는 작업을 선택하세요 (1-5): ")
    
    if choice == '1':
        name = input("이름을 입력하세요: ").strip()
        phone = input("전화번호를 입력하세요: ").strip()
        contacts[name] = phone
        print(f"{name}의 연락처가 추가되었습니다.")
        
    elif choice == '2':
        name = input("조회할 이름을 입력하세요: ").strip()
        if name in contacts:
            print(f"{name}의 전화번호는 {contacts[name]}입니다.")
        else:
            print(f"{name}의 연락처가 없습니다.")
    elif choice == '3':
        name = input("삭제할 이름을 입력하세요: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"{name}의 연락처가 삭제되었습니다.")
        else:
            print(f"{name}의 연락처가 없습니다.")
    elif choice == '4':
        if contacts:
            print("모든 연락처 목록:")
            for name, phone in contacts.items():
                print(f"이름: {name}, 전화번호: {phone}")
        else:
            print("저장된 연락처가 없습니다.")
    elif choice == '5':
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 선택을 하세요 (1-5).")



