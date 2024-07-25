num = 1
min_num = 0

while num <= 150:
    if num % 5 == 0 and num % 8 == 0:
        print('공배수:', num)
        if min_num == 0: min_num = num
    num += 1

print('최소공배수:', min_num)



