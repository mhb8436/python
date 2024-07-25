length = 1
max_area = 200

while True:    
    length = length * 3
    area = length * length 
    if area > max_area: 
        break
    print(f"한변의 길이 : {length}, 사각형의 넓이 : {area}")

print('exit program')

