# Process 2
import os
import stat
import time

fifo = "fifo"

if not os.path.exists(fifo):
    os.mkfifo(fifo, stat.S_IRUSR | stat.S_IWUSR)

fd = os.open(fifo, os.O_RDWR)

while True:
    message = os.read(fd, 100).decode()
    print("Message received by Process B : ", message)

    if message.strip() == 'STOP':
        print('Communication Break !!!')
        break

    message = input("Enter a message for the Process 1 ('STOP' to quit): ")

    os.write(fd, message.encode())
    if message.strip() == 'STOP':
        print('Communication Break !!!')
        break

time.sleep(1)

os.close(fd)
if os.path.exists(fifo):
    os.unlink(fifo)
