import module04.square as s

h = int(input('높이를 입력하세요:'))
b = int(input('밑변 길이를 입력하세요'))

l = s.length(h, b)
a = s.area(h, b)

print(f"사각형 ( {h} x {b} ) 의 둘레 길이는 {l} 이고 넓이는 {a} 입니다.")


