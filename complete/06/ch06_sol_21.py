mood = input("지금 기분은 어떤가요? (행복, 슬픔, 신남): ")

if mood == "행복":
    print("추천 음악: Pharrell Williams - Happy")
elif mood == "슬픔":
    print("추천 음악: Adele - Someone Like You")
elif mood == "신남":
    print("추천 음악: Bruno Mars - Uptown Funk")
else:
    print("올바른 기분을 입력하세요.")
