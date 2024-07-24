time = int(input("현재 시간을 입력하세요 (24시간 형식): "))

if 6 <= time < 10:
    print("추천 아침 메뉴: 토스트와 커피")
elif 10 <= time < 12:
    print("추천 아침 메뉴: 시리얼과 우유")
else:
    print("지금은 아침 시간이 아닙니다.")
