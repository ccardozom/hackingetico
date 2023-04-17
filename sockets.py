import socket

try:
    print("gethostbyname")
    print(socket.gethostbyname("www.l.com"))
    print("\ngethostbyaddr")
    print(socket.gethostbyaddr('142.250.200.132'))
    print("\ngetfqdn")
    print(socket.getfqdn('www.google.com'))
except socket.error as error:
    print(str(error))