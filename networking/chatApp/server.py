import socket

HOST = '127.0.0.1' # loopback address(local machine)
PORT = 8000   # any port number is fine


#socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the address
server_socket.bind((HOST, PORT))

#listen for incoming connections
server_socket.listen()

# print(f"Server is listening on {HOST}:{PORT}")


#Accept incoming connections
client_socket, client_address = server_socket.accept()
print("Connected with", client_address)

#Receive data from the client
while True:
    message = input("You: ")
    client_socket.sendall(message.encode('utf-8'))
    if message.lower() == "exit":
        break
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Sender: {data}")
    
    


#Close the connection
client_socket.close()
server_socket.close()
    
    