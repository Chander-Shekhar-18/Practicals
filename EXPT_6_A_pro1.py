import socket

def main():
    recevfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('', 5000)
    recevfd.bind(server)

    while True:
        rcv, client = recevfd.recvfrom(1024)
        rcv = rcv.decode()

        if rcv == "stop" or rcv == "STOP":
            print("Communication Break !!!")
            break

        print("Client : ", rcv)
        snd = input("Enter a message for Sender : ")
        recevfd.sendto(snd.encode(), client)

        if snd == "stop" or snd == "STOP":
            print("Communication Break !!!")
            break

    recevfd.close()

if __name__ == "__main__":
    main()

