import socket  # Import the socket module for network communication

# Create a socket object for the client
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Connect the client to the server's IP and port
c.connect(('192.168.56.1', 56))  

# Receive the message from the server and decode it to a readable format
print(c.recv(1024).decode())  

# Close the connection
c.close()