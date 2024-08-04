sum = 0
def add(n):
    if n < 101:
        global sum
        sum += n
        print('number =>', n)
        add(n+1)

add(1)
print('sum => ', sum)


