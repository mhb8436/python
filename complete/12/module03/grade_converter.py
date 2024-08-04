grades = {
    'A': (90, 100),
    'B': (80, 90),
    'C': (70, 80),
    'D': (60, 70),
    'F': (0, 60),
}

def convert_score_to_grade(score):
    if score < 0 or score > 100:
        print('점수는 0 부터 100 사이어야 합니다')
        return 
    
    for grade, (low, high) in grades.items():    
        if low <= score < high: 
            return grade
    
    return "F"

def grade_description(grade):
    description = {
        'A':"훌륭합니다",
        'B':"좋습니다.",
        'C':"괜찮습니다.",
        'D':"촘 더 노력하세요",
        'F':"불합격입니다. 노력하세요",
    }
    return description[grade]

