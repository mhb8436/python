import socket
import threading

# 서버 설정
HOST = '127.0.0.1'  # localhost
PORT = 12345

# 클라이언트 핸들러 함수
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received: {message}")
            broadcast(message, client_socket)
        except:
            break
    client_socket.close()

# 메시지를 모든 클라이언트에게 전송하는 함수
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# 소켓 생성 및 설정
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

while True:
    client_socket, addr = server.accept()
    print(f"Connection established with {addr}")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()




