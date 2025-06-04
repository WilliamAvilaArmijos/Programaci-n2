

import socket

# Definir el host y el puerto
host = 'www.facebook.com'  
port = 80  # Puerto HTTP

# Crear un socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Intentar conectarse al host y puerto
    sock.connect((host, port))
    print("c", host)
except socket.error as e:
    print("Error de conexión:", e)
finally:
    
    sock.close()
