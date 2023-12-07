import os
import sys

if __name__ == "__main__":
    pipe_fd1 = os.pipe()
    pipe_fd2 = os.pipe()

    pid1 = os.fork()

    if pid1 == 0:
        # This is child 1
        os.close(pipe_fd1[0])
        os.close(pipe_fd2[1])

        while True:
            message = input("Enter a message for Child Process 2: ")
            os.write(pipe_fd1[1], message.encode())

            if message.rstrip() == "STOP":
                print("Communication break by Child Process 1 !!!")
                sys.exit(0)

            byteMsgFromParent = os.read(pipe_fd2[0], 100)
            msgFromParent = byteMsgFromParent.decode('utf-8')

            if msgFromParent.rstrip() == "STOP":
                os.close(pipe_fd1[1])
                os.close(pipe_fd2[0])
                sys.exit(0)
            else:
                print("Received message from Child Process 2 : ", msgFromParent)
        
    else:
        # This is the parent
        pid2 = os.fork()
        if pid2 == 0:
            # This is child 2
            os.close(pipe_fd1[1])
            os.close(pipe_fd2[0])

        while True:
            byteMsgFromChild = os.read(pipe_fd1[0], 100)
            msgFromChild = byteMsgFromChild.decode('utf-8')

            if msgFromChild.rstrip() == "STOP":
                os.close(pipe_fd1[0])
                os.close(pipe_fd2[1])
                sys.exit(0)
            else:
                print("Received message from Child Process 1: ", msgFromChild)

            message = input("Enter a message for Child Process 1 : ")
            os.write(pipe_fd2[1], message.encode())

            if message.rstrip() == "STOP":
                print("Communication break by Parent Process 2 !!!")
                sys.exit(0)