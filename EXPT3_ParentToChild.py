import os
import sys

def main():
    pipe_fd1 = os.pipe()
    pipe_fd2 = os.pipe()

    child_pid = os.fork()

    if child_pid == 0:
        os.close(pipe_fd1[0])
        os.close(pipe_fd2[1])

        while True:
            message = input("Enter a message for parent: ")
            os.write(pipe_fd1[1], message.encode())

            if message.rstrip() == "STOP":
                print("Communication break by Child Process !!!")
                sys.exit(0)

            byteMsgFromParent = os.read(pipe_fd2[0], 100)
            msgFromParent = byteMsgFromParent.decode('utf-8')

            if msgFromParent.rstrip() == "STOP":
                os.close(pipe_fd1[1])
                os.close(pipe_fd2[0])
                sys.exit(0)
            else:
                print("Received message from parent: ", msgFromParent)

    else:
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
                print("Received message from child: ", msgFromChild)

            message = input("Enter a message for child: ")
            os.write(pipe_fd2[1], message.encode())

            if message.rstrip() == "STOP":
                print("Communication break by Parent Process !!!")
                sys.exit(0)

if __name__ == "__main__":
    main()