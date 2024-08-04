scores = {
    'java': 80,
    'python': 90,
    '모바일':60,
    '보안': 70
}
scores['시스템'] = 85
print(scores['java'])
scores['모바일'] = 82
scores['시스템'] = 75 
sum = 0
for k in scores.keys():
    sum += scores[k]
    print(k, '=>', scores[k])

print('평균점수 :' , sum/len(scores.keys()))



