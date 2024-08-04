# 학생 성적 딕셔너리
grades = {}

# 메인 프로그램
while True:
    print("\n1. 성적 추가")
    print("2. 성적 조회")
    print("3. 성적 업데이트")
    print("4. 성적 삭제")
    print("5. 모든 성적 출력")
    print("6. 종료")
    
    choice = input("원하는 작업을 선택하세요 (1-6): ")
    
    if choice == '1':
        student_name = input("학생 이름을 입력하세요: ").strip()
        subject = input("과목명을 입력하세요: ").strip()
        score = int(input(f"{subject} 성적을 입력하세요: ").strip())
        if student_name not in grades:
            grades[student_name] = {}
        grades[student_name][subject] = score
        print(f"{student_name}의 {subject} 성적이 추가되었습니다: {score}점")
    elif choice == '2':
        student_name = input("학생 이름을 입력하세요: ").strip()
        subject = input("조회할 과목명을 입력하세요: ").strip()
        
        if student_name in grades and subject in grades[student_name]:
            print(f"{student_name}의 {subject} 성적: {grades[student_name][subject]}점")
        else:
            print(f"{student_name}의 {subject} 성적이 없습니다.")
    elif choice == '3':
        student_name = input("학생 이름을 입력하세요: ").strip()
        subject = input("과목명을 입력하세요: ").strip()
        score = int(input(f"새로운 {subject} 성적을 입력하세요: ").strip())
        if student_name in grades and subject in grades[student_name]:
            grades[student_name][subject] = score
            print(f"{student_name}의 {subject} 성적이 업데이트되었습니다: {score}점")
        else:
            print(f"{student_name}의 {subject} 성적이 없습니다. 먼저 추가해주세요.")
    elif choice == '4':
        student_name = input("학생 이름을 입력하세요: ").strip()
        subject = input("삭제할 과목명을 입력하세요: ").strip()
        if student_name in grades and subject in grades[student_name]:
            del grades[student_name][subject]
            print(f"{student_name}의 {subject} 성적이 삭제되었습니다.")
            if not grades[student_name]:  # 해당 학생의 모든 과목이 삭제된 경우
                del grades[student_name]
        else:
            print(f"{student_name}의 {subject} 성적이 없습니다.")
    elif choice == '5':
        if grades:
            print("모든 학생의 성적 목록:")
            for student_name, subjects in grades.items():
                print(f"\n학생: {student_name}")
                for subject, score in subjects.items():
                    print(f"  과목: {subject}, 성적: {score}점")
        else:
            print("저장된 성적이 없습니다.")
    elif choice == '6':
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 선택을 하세요 (1-6).")



