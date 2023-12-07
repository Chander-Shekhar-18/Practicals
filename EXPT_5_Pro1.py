import sysv_ipc
import os

key = sysv_ipc.ftok("keyfile", 65)
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

while True:
    message = input("Enter a message to send (or type 'STOP' to quit): ")

    mq.send(message)

    if message.strip() == 'STOP':
        print("Communication Break !!!")
        break

    message, _ = mq.receive()
    print("Received reply: ", message.decode())

    if message.decode().strip() == 'STOP':
        print("Communication Break !!!")
        break

mq.remove()
