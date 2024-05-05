import socket

# Define host and port to listen on
host = '0.0.0.0'  # Listen on all available network interfaces
port = 12345      # Choose any available port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on port", port)

# Accept incoming connection
client_socket, client_address = server_socket.accept()
print("Connection from:", client_address)

# Receive and print messages
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print("Received message:", data)

# Close the connection
client_socket.close()
server_socket.close()
