import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

clients = []

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if data == 'STOP':
            print(f"Client {client_socket.getpeername()} has requested to STOP.")
            break
        print(f"Received from {client_socket.getpeername()}: {data}")
        response = input("Enter your response: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

except KeyboardInterrupt:
    print("Server shutting down.")
    for client in clients:
        client.send("STOP".encode('utf-8'))
        client.close()
    server.close()