scores = [70, 35, 40, 90]
total, under, average = 0,0,0

for s in scores:
    if s < 40:
        under += 1
    total += s

print('40미만 과목수 =>', under)
average = total / len(scores)
print('평균점수=>', average)

if under > 0 or average < 60:
    print('불합격')
else:
    print('합격')



