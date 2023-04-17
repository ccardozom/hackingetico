#!/usr/bin/python
#tcpserver.py

import socket

host= 'localhost'
port = 1337
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(3)
print("Servidor escuchando peticiones en el puerto {}".format(port))
while 1:
    cli,addr = sock.accept()
    print("Se ha producido una conexion desde {}".format(addr))
    buf = cli.recv(1024)
    print(f"Mensaje recibido: {buf}")
    if buf == "Hello\n".encode():
        cli.send("Hola, viajante del espacio!!".encode())
    cli.close()
