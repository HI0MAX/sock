import socket

# Define server address and port
server_address = 'SERVER_PUBLIC_IP'  # Replace with the server's public IP address
server_port = 12345                  # Replace with the server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((server_address, server_port))

# Send a message
message = "Hello from the client!"
client_socket.send(message.encode())

# Close the connection
client_socket.close()
