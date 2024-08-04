import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen()
while True:
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)        
            if not data:
                break
            print(f"클라이언트로부터 받은 데이터 : {data.decode()}")
            msg = f"Hello Client({addr})"
            conn.sendall(bytes(msg,'utf-8'))

