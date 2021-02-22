import socket


PORT = 30000
#SERVER = socket.gethostbyname(socket.gethostname())
#ADDR = (SERVER,PORT)

#STEP 1 - create the socket object. This example uses TCP over IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#STEP 2 - connect!

server_address = ('localhost', PORT)
print("Connecting to...", server_address)
sock.connect(server_address)

print("Yay! connected to...", server_address)

#step 3 - send BINARY data
data = b"Hello server!"
print("Sending message...", data)
sock.sendall(data)
sock.close()

