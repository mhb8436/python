# 학생 데이터 (이름, 학번, 수학 성적, 과학 성적, 영어 성적)
student1 = ("민지", "202401", 85, 92, 88)
student2 = ("혜린", "202402", 78, 85, 80)
student3 = ("하니", "202403", 90, 87, 93)

students = [student1,student2,student2]

# 학생별 평균 성적
for student in students:
    sum_score = student[2] + student[3] + student[4]
    avg_score = sum_score / 3
    print(student[0], '의 평균점수 =>', format(avg_score, '.2f'))

sum_math_score = 0 # 수학 총점
sum_sci_score = 0  # 과학 총점
sum_eng_score = 0  # 영어 총점 

for student in students:
    sum_math_score += student[2]
    sum_sci_score += student[3]
    sum_eng_score += student[4]

print('수학 평균 =>', format(sum_math_score / 3, '.2f'))
print('과학 평균 =>', format(sum_sci_score / 3, '.2f'))
print('영어 평균 =>', format(sum_eng_score / 3, '.2f'))


