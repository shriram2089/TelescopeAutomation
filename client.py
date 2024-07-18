import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the ESP32 server
sock.connect(('192.168.0.236', 80))  # Replace ESP32_IP_ADDRESS with the actual IP address of your ESP32

# Send data to the ESP32
sock.send(b'Hello, ESP32!')

# Receive data from the ESP32
data = sock.recv(1024)

# Close the socket connection
sock.close()

# Print the data received from the ESP32
print("Response from ESP32:", data.decode())
