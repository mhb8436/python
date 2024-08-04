def calc(a, b):
    r1 = a + b
    r2 = a - b
    r3 = a * b 
    r4 = a / b
    return (r1, r2, r3, r4)

a = int(input('값을 입력하세요'))
b = int(input('값을 입력하세요'))

result = calc(a, b)
print(result)