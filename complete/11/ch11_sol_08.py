student_scores = [
    {'이름':'민지', '학번':'24092801', '수학':80, '과학':100, '영어':50},
    {'이름':'하니', '학번':'24092802', '수학':65, '과학':80, '영어':70},
    {'이름':'다니엘', '학번':'24092803', '수학':90, '과학':72, '영어':90},
    {'이름':'혜인', '학번':'24092804', '수학':100, '과학':50, '영어':50},
    {'이름':'해린', '학번':'24092804', '수학':75, '과학':100, '영어':90},
]

print("-"*30)
print("학생별 성적")
print("-"*30)

for student in student_scores:
    s_total = student['수학'] + student['과학'] + student['영어']
    s_avg = s_total / 3
    print(f"{student['이름']} 의 총점은 {s_total} 점이고 평균은 {s_avg:.2f} 입니다")

print("-"*30)

print("-"*30)
print("과목별 평균 성적")
print("-"*30)

math_total = 0
sci_total = 0
eng_total = 0

for student in student_scores:
    math_total += student['수학']
    sci_total += student['과학']
    eng_total += student['영어']

print(f"수학 평균 성적: {math_total / len(student_scores)}")
print(f"과학 평균 성적: {sci_total / len(student_scores)}")
print(f"영어 평균 성적: {eng_total / len(student_scores)}")
