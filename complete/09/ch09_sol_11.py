quiz1 = ('3+2', 3+2, 4)
quiz2 = ('5*8', 5*8, 4)
quiz3 = ('10-3', 10-3, 4)
quiz4 = ('3^3', 3^3, 4)
quiz5 = ('6/2', 6/2, 4)

quiz = [quiz1, quiz2, quiz3, quiz4, quiz5]
answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in quiz:
    print('문제: ', item[0])
    answer = int(input('정답을 입력하세요 => '))
    if answer == item[1]:
        answerCount += 1
        totalScore += item[2]
    else:
        wrongAnswerCount += 1

print('-'*30)
print('정답개수\t:', answerCount)
print('오답개수\t:', wrongAnswerCount)
print('전체점수\t:', totalScore)
print('-'*30)

