#!/usr/bin/python
#tcpclient.py

import socket
import httplib2

host = "localhost"
port = 1337

try: 
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect_ex((host,port))
    print("Conectado al host " + str(host + " en el puerto " + str(port)))
    mysocket.send("Hello\n".encode())
    mensaje = mysocket.recv(1024)
    print("Recibido", mensaje)
    msg = "Mensaje del cliente\n"
    mysocket.sendall(msg.encode())
except socket.error as e:
    print("Socket error: ", e)
finally:
    mysocket.close()