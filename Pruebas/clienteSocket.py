import socket

clienteSocket = socket.socket()
clienteSocket.connect(("localhost", 2018))

clienteSocket.send(b'Hola desde el cliente') #mandamos mensaje al servidor

respuesta = clienteSocket.recv(1024) #recibe datos del servidor

print (respuesta)

clienteSocket.close()

