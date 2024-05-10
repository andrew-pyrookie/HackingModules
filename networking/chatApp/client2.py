import socket

# define address and port 
HOST = '127.0.0.1'
PORT = 8001 

#create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the server
client_socket.connect((HOST,PORT))
print(f"Connected with {HOST}:{PORT}")

#send data to the server
while True:
    message = input("You : ")
    client_socket.sendall(message.encode('utf-8'))
    if message.lower() == "exit":
        break
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Sender : {data}")
    
client_socket.close()