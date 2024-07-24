purchase_amount = int(input('구매금액을 입력하세요'))
membership_level = input('회원등급을 입력하세요')

discount = 0.0
discountAmount = 0.0

if membership_level == '골드':
    if purchase_amount > 10:
        discount = 0.2
    elif purchase_amount > 5 and purchase_amount <= 10:
        discount = 0.1
    else:
        discount = 0.05
elif membership_level == '실버':
    if purchase_amount > 10:
        discount = 0.15
    elif purchase_amount > 5 and purchase_amount <= 10:
        discount = 0.07
    else:
        discount = 0.03
elif membership_level == '일반':
    if purchase_amount > 10:
        discount = 0.1
    elif purchase_amount > 5 and purchase_amount <= 10:
        discount = 0.05
    else:
        discount = 0.00

discountAmount = purchase_amount * discount
finalAmount = purchase_amount - discountAmount
freeship = False

if purchase_amount >= 70000:
    freeship = True

print('구매금액:', purchase_amount)
print('할인금액:', discountAmount)
print('결제금액:', finalAmount)
print('할인율:', discount * 100 , '%')
print('무료배송:', '무료배송' if freeship else '유료배송')
