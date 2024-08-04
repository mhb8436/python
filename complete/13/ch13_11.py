file = open('../num.txt','r')
result = file.read()
print(f"result => {result}")
sum = result + 10
print(f"sum => {sum}")
file.close()


