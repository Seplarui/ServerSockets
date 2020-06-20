import socket

host = socket.gethostname()  # nombre del host

port = 2018

BUFFER_SIZE = 1024  # tamaño máximo del paquete

# Objeto tipo socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port))
    socket_tcp.listen(5)  # esperamos conexión del cliente
    conn, addr = socket_tcp.accept() #Conexión con el cliente
    with conn:
        print('[*] Conexión establecida')
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            else:
                print('[*] Datos recibidos: {}'.format(data.decode('utf-8')))
            conn.send(data) 

