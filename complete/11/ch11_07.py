def findMax(*nums):
    print(type(nums))

    max = 0
    for n in nums:
        if n > max:
            max = n

    print('최대값 :', max ) 

findMax(10,20,30)
findMax(10,20,30,40)
findMax(10,20,30,40,50)
findMax(10,20,30,40,50,60)

