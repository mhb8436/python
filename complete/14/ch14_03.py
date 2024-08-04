import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8001))
print('UDP 서버가 시작되었습니다. 클라이언트 메시지를 기다립니다')
while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"클라이언트 {addr}로 부터 받은 메시지 : {data.decode()}")
    message = f"Hello, Client {addr}"
    server_socket.sendto(message.encode(), addr)



