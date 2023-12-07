import rpyc
from rpyc.utils.server import ThreadedServer


class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_add(self, x, y): 
        return x + y

    def exposed_sub(self, x, y): 
        return x - y

    def exposed_mul(self, x, y): 
        return x * y

    def exposed_div(self, x, y): 
        return x / y if y != 0 else 'Error: Division by zero'

if __name__ == "__main__":
    t = ThreadedServer(MyService, port = 18862)
    print('Server started on port 18862')
    t.start()
