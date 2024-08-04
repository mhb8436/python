# import socket

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client_socket.connect(('localhost', 65432))
# client_socket.sendall(b"Hello Server")
# data = client_socket.recv(1024)
# print(f"서버로부터 받은 데이터 : {data.decode()}")
# client_socket.close()

import socket

# 서버 정보 설정
HOST = '127.0.0.1'  # 서버의 호스트
PORT = 65432       # 서버의 포트 번호

# 소켓 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # 서버에 연결
    s.sendall(b'Hello, world')  # 데이터 전송
    data = s.recv(1024)  # 데이터 수신

print('Received', repr(data))
