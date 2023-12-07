import sysv_ipc

key = sysv_ipc.ftok("keyfile", 65)
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

while True:
    message, _ = mq.receive(type=1)
    print("Received message: ", message.decode())

    if message.decode().strip() == 'STOP':
        print("Communication Break !!!")
        break

    reply = input("Enter a reply (or type 'STOP' to quit): ")

    mq.send(reply, type=2)

    if reply.strip() == 'STOP':
        print("Communication Break !!!")
        break
