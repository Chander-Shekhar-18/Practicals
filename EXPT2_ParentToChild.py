import os

def parent_child_communication():
    r, w = os.pipe()
    pid = os.fork()

    if pid:
        os.close(r)
        msg = input("Enter message :")
        byteString = bytes(msg,'utf-8')
        os.write(w, byteString)
        os.close(w)
    else:
        os.close(w)
        message = os.read(r, 1024)
        print(f'Child received: {message}')
        os.close(r)  


if __name__ == '__main__':
    parent_child_communication()