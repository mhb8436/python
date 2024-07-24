height = int(input('신장을 입력하세요'))
# print(height >= 120 and height < 170)



# print( 170 >= height > 120 )

result = '키가커요' if height > 170 else '키가너무 작아요' if height < 120 else '탑승가능'
print(result)