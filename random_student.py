import random

def choose_random_student(filename):
    try:
        # 텍스트 파일에서 학생 이름을 읽어 리스트로 저장
        with open(filename, 'r') as file:
            students = file.read().splitlines()
        
        if not students:
            raise ValueError("파일에 학생 이름이 없습니다.")
        
        # 무작위로 학생 선택
        selected_student = random.choice(students)
        return selected_student
    
    except FileNotFoundError:
        return "파일을 찾을 수 없습니다."
    except Exception as e:
        return f"오류가 발생했습니다: {e}"

if __name__ == "__main__":
    filename = 'students.txt'
    selected_student = choose_random_student(filename)
    print(f"발표할 학생: {selected_student}")

