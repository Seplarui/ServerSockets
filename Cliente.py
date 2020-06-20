import socket

host = socket.gethostname()
port = 2018
BUFFER_SIZE = 1024

MESSAGE = "CLIENTE DICE: Hola Mundo!"  # Datos que enviamos al servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    socket_tcp.send(MESSAGE.encode('utf-8'))
    data = socket_tcp.recv(BUFFER_SIZE)
