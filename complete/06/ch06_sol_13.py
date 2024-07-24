purchase = int(input('구매금액을 입력하세요'))

discount = 0.0
discountAmount = 0.0

if purchase >= 200000:
    discount = 0.25
elif purchase >= 100000 and purchase < 200000:
    discount = 0.20
elif purchase >= 50000 and purchase < 100000:
    discount = 0.15
elif purchase < 50000:
    discount = 0.10

print('구매금액: ', purchase)
print('할인율 :', discount * 100,'%')
print('최종금액: ', purchase - purchase * discount)


