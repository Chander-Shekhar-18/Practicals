import socket

# Client configuration
HOST = '127.0.0.1'
PORT = 5555

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

try:
    while True:
        message = input("Enter your message for Server : ")
        client.send(message.encode('utf-8'))
        if message == 'STOP':
            break

        response = client.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

except KeyboardInterrupt:
    print("Client shutting down.")
    client.send("STOP".encode('utf-8'))

finally:
    client.close()
