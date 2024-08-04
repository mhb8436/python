# 메뉴 항목을 튜플로 정의 (이름, 가격, 카테고리)
menu_item1 = ("파스타", 12500, "Main Course")
menu_item2 = ("시저셀러드", 8000, "Appetizer")
menu_item3 = ("초콜릿 케익", 6500, "Dessert")
menu_item4 = ("스테이크", 20000, "Main Course")
menu_item5 = ("마늘빵", 4500, "Appetizer")
menu_item6 = ("아이스크림", 5000, "Dessert")

# 메뉴 항목을 리스트에 저장
menu = [menu_item1, menu_item2, menu_item3, menu_item4, menu_item5, menu_item6]
  

# 사용자로부터 카테고리 입력 받기
category = input("메뉴 카테고리를 입력하세요 (Appetizer, Main Course, Dessert): ")

print(f"{category} 메뉴:")
for item in menu:
    name, price, item_category = item
    if item_category == category:
        print(f"이름: {name}, 가격: {price:.2f} 원")

