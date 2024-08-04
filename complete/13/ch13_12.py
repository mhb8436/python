file = open('../num.txt','r')
result = file.read()
print(f"result => {result}")
sum = int(result) + 10
print(f"sum => {sum}")
file.close()


