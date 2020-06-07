import socket

serverSocket = socket.socket()
serverSocket.bind(('localhost', 2018))
serverSocket.listen(5)

while True:
    conexion, addr = serverSocket.accept()
    print ('Nueva conexión')
    print (addr)

    conexion.send("Hola desde el serviro") #Envio mensaje al cliente
    conexion.close()
    
