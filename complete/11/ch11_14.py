def calc(a, b):
    def add(x,y):
        return a + b
    def subtract(x, y):
        return a - b
    def multiply(x, y):
        return a * b
    def divide(x, y):
        return a / b
    
    r1, r2, r3 ,r4 = add(a,b), subtract(a,b),multiply(a,b), divide(a,b)
    return (r1, r2, r3, r4)

a = int(input('값을 입력하세요'))
b = int(input('값을 입력하세요'))

result = calc(a, b)
print(result)


