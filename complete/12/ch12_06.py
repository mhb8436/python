import os

print(os.getcwd()) # 현재 디렉토리 출력
os.mkdir('new_folder') # 새로운 디렉토리 생성

path = "/Users/mhb8436/Downloads" 
print(os.path.exists(path)) # 디렉토리 존재 여부 확인 

path = "/Users/mhb8436/Downloads" 
dir_list = os.listdir(path) # 디렉토리 내용 출력
for item in dir_list:
    print(item)