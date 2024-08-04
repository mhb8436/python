file = open('../test.txt','r')
result = file.read()
print(f"type of result => {type(result)}")
print(f"result => {result}")
file.close()


