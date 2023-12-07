import socket

def main():
    sendfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('localhost', 5000)

    while True:
        snd = input("Enter a for the Client : ")
        sendfd.sendto(snd.encode(), server)

        if snd == "stop":
            print("Communication Break !!!")
            break

        rcv, client = sendfd.recvfrom(1024)
        rcv = rcv.decode()

        if rcv == "stop" or rcv == "STOP":
            print("Communication Break !!!")
            break
            
        print("Message received by Server : ", rcv)

    sendfd.close()

if __name__ == "__main__":
    main()

