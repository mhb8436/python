def findMin(*nums):
    min = nums[0]
    for n in nums:
        if n < min:
            min = n
    print(nums, ' => 최소값 :', min ) 

def findAvg(*nums):
    total = 0
    for n in nums:
        total += n

    print(nums, ' => 평균값 :', total/len(nums)) 

findMin(10,20,30, 2)
findMin(10,20,30,40, 3)
findMin(10,20,30,40,50,4)
findMin(10,20,30,40,50,60,2)
print('----------')
findAvg(10,20,30)
findAvg(10,20,30,40)
findAvg(10,20,30,40,50)
findAvg(10,20,30,40,50,60)


