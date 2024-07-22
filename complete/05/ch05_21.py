targetScore = 90
myScore = int(input('점수를 입력하세요:'))
result = 0
if myScore >= targetScore:
    result = "pass"
else:
    result = "fail"
print('시험결과: ', result) 


