import socket

PORT = 30000
#SERVER = socket.gethostbyname(socket.gethostname())
#ADDR = (SERVER,PORT)

#STEP 1 - create the socket object. This example uses TCP over IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#STEP 2 - specify where the server should listen on, IP and PORT
server_address_object = ('localhost', PORT)
print("Address = ", server_address_object)
sock.bind(server_address_object)

#STEP 3 - do the actual listening
sock.listen(1)

#STEP 4 - wait for connection from client! This is a blocking call!!!!

print("Waiting to hear from a client.....")
connection_object, client_address = sock.accept()

print("Yay! Heard from a client, address is:", client_address)


#step 5 - keep listening, how much can you receive? Try setting it to 1
with connection_object as conn_obj:
    try:
        data_from_client = conn_obj.recv(1024)
        print("Data = ", data_from_client.decode())
    except KeyboardInterrupt: #CTRL+^C
        sock.close()

