import module03.grade_converter

while True:
    score = float(input('학생 성적을 입력하세요(종료하려면 -1을 입력하세요):'))
    if score == -1:
        print('프로그램을 종료합니다')
        break

    grade = module03.grade_converter.convert_score_to_grade(score)
    description = module03.grade_converter.grade_description(grade)
    print(f"학생의 점수: {score}, 등급 : {grade}, 설명: {description}")



    