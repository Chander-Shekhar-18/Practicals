import os

def child1(w):
    os.close(w[0]) 
    message = input('Enter your message :')
    print()
    os.write(w[1], message.encode())
    os.close(w[1])

def child2(r):
    os.close(r[1]) 
    message = os.read(r[0], 1024)
    os.close(r[0])
    print("Message recieved by child 2 :", message.decode())

if __name__ == "__main__":
    r, w = os.pipe()
    pid1 = os.fork()
    if pid1 == 0:
        # This is child 1
        print('Process id of child 1 is :', os.getpid())
        print('Parent id of child 1 is :', os.getppid())
        child1((r, w))
        os._exit(0)
    else:
        # This is the parent
        pid2 = os.fork()
        if pid2 == 0:
            # This is child 2
            child2((r, w))
            print('Process id of child 2 is :', os.getpid())
            print('Parent id of child 2 is :', os.getppid())
            os._exit(0)
        else:
            # This is the parent
            os.close(r)
            os.close(w)
            os.waitpid(pid1, 0)
            os.waitpid(pid2, 0)