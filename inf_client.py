import socket
import time

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the ESP32 server
sock.connect(('192.168.0.236', 80))  # Replace ESP32_IP_ADDRESS with the actual IP address of your ESP32

try:
    while True:
        # Send data to the ESP32
        #message = input("Enter message to send: ")/
        message = "hello"
        sock.send(message.encode())

        # Receive data from the ESP32
        data = sock.recv(1024)

        # Print the data received from the ESP32
        print("Response from ESP32:", data.decode())

        # Wait for a short time before sending the next message
        time.sleep(1)
except KeyboardInterrupt:
    print("Client terminated by user.")
finally:
    # Close the socket connection
    sock.close()
