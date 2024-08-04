# import socket

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 8000))
# server_socket.listen()
# print('서버가 시작되었습니다. 클라이언트 연결을 기다립니다')
# client_socket, addr = server_socket.accept()
# try:                
#     data = client_socket.recv(1024)
#     print(f"클라이언트로부터 받은 데이터 : {data.decode()}")
#     client_socket.sendall(b"Hello Client~")
# except:
#     pass
# finally:
#     client_socket.close()
#     server_socket.close()

import socket

# 서버 정보 설정
HOST = '127.0.0.1'  # 로컬 호스트
PORT = 65432       # 사용할 포트 번호

# 소켓 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # 소켓을 주소에 바인딩
    s.listen()            # 클라이언트의 연결 요청을 대기

    print(f"Server started at {HOST}:{PORT}")
    
    conn, addr = s.accept()  # 연결 승인
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)  # 데이터 수신
            if not data:
                break
            conn.sendall(data)  # 데이터 전송 (에코)
