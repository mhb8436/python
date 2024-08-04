import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8001)
message = "Hello Server"
client_socket.sendto(message.encode(), server_address)
data, server = client_socket.recvfrom(1024)
print(f"서버로부터 받은 메시지 : {data.decode()}")
client_socket.close()




