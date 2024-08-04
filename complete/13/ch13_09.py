file = open('../test.txt','w')
result = file.write('Hello Python')
print(f"type of result => {type(result)}")
print(f"result => {result}")
file.close()



