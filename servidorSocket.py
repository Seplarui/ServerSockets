import socket

serverSocket = socket.socket()
serverSocket.bind(('localhost', 2018))
serverSocket.listen(5)

while True:
    conexion, addr = serverSocket.accept()
    print ('Nueva conexión')
    print (addr)
    print(conexion)

    conexion.send(b'Hola desde el servidor') #Envio mensaje al cliente
    conexion.close()
    
