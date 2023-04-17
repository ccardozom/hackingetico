import socket
import sys

def checkPortsSocket(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.03)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Puerto {port}: \t Abierto")
            else:
                print(f"Puerto {port}: Cerrado")
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Error de conexion")
        sys.exit()
        
hostname = socket.gethostbyname("www.google.com")
print(hostname)
checkPortsSocket(hostname, [80,8080,443])