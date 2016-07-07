from socketIO_client import SocketIO, BaseNamespace


class Handlers(BaseNamespace):

    def on_message_from_server(self, msg):
        print("Incoming msg: %s" % msg)


io = SocketIO('localhost', 9090, Handlers, resource="api/v1/socket")

io.emit('hello_from_client')

io.wait(seconds=10)

