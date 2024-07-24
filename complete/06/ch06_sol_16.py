k_score = int(input('국어 점수를 입력하세요'))
e_score = int(input('영어 점수를 입력하세요'))
m_score = int(input('수학 점수를 입력하세요'))

avg = ( k_score + e_score + m_score ) / 3

if avg >= 60 and avg < 100:
    print('A')   
else:
    print('F')   


