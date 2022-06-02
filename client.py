import socket

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(b"Server va mijoz ulandi")

    data = client_socket.recv(1024)
    print("Habar: ", repr(data))

