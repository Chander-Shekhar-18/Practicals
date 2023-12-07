# Process 1
import os
import stat

fifo = "fifo"

os.mkfifo(fifo, stat.S_IRUSR | stat.S_IWUSR)

fd = os.open(fifo, os.O_RDWR)

while True:
    message = input("Enter a message for the process B ('STOP' to quit) : ")

    os.write(fd, message.encode())

    if message.strip() == 'STOP':
        print('Communication Break !!!')
        break

    message = os.read(fd, 100).decode()
    print("Message received by Process A : ", message)

    if message.strip() == 'STOP':
        print('Communication Break !!!')
        break

os.close(fd)
if os.path.exists(fifo):
    os.unlink(fifo)
