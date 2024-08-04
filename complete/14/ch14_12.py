import socket
import threading

# 서버 설정
HOST = '127.0.0.1'  # 서버 IP 주소
PORT = 12345

# 서버로부터 메시지를 수신하는 함수
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Server: {message}")
        except:
            break

# 소켓 생성 및 서버에 연결
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# 메시지 수신용 쓰레드 시작
threading.Thread(target=receive_messages, args=(client,)).start()

# 사용자 입력을 서버로 전송
while True:
    message = input()
    client.send(message.encode('utf-8'))



