num = 1
sum = 0

while num < 11:
    print(num, sum)
    sum += num
    if sum >= 30:
        print('num =>', num)
        break
    num += 1


