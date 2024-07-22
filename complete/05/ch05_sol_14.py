membership_level = "골드"
purchase_amount = 100000 
level = input('등급을 입력하세요:')
purchase = int(input('구매금액을 입력하세요'))
result = membership_level == "골드" or purchase_amount >= purchase
print("할인쿠폰제공여부", result)

