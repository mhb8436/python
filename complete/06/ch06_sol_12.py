membership_level = input('회원등급을 입력하세요')

discount = 0.0
discountAmount = 0.0

if membership_level == '플래티넘':
    discount = 0.25
elif membership_level == '골드':
    discount = 0.20
elif membership_level == '실버':
    discount = 0.15
elif membership_level == '일반':
    discount = 0.10

print('할인쿠폰 :', discount * 100
      , '% 이 발급되었습니다')

