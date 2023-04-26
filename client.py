import socket

# Initialize Socket Instance
sock = socket.socket()
print ("Socket creado exitosamente.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Conección Establecida.')
# Send a greeting to the server
sock.send('Recibió un mensaje por parte del cliente'.encode())

# Write File in binary
file = open('client-file.txt', 'wb')

# Keep receiving data from the server
line = sock.recv(1024)

while(line):
    file.write(line)
    line = sock.recv(1024)

print('El archivo se ha transferido correctamente.')

file.close()
sock.close()
print('Connection Closed.')
