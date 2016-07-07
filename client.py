from socketIO_client import SocketIO, BaseNamespace


class Handlers(BaseNamespace):

    def on_message_from_server(self, msg):
        print("Incoming msg: %s" % msg)


class ApiHandlers(BaseNamespace):

    def on_ping(self, msg):
        print("PONG %s" % msg)


io = SocketIO('localhost', 9090, Handlers)
#io_api = io.define(ApiHandlers, '/api/v1/socket')

io.emit('hello_from_client')
#io_api.emit('ping')

io.wait(seconds=10)

