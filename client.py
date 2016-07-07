from socketIO_client import SocketIO

io = SocketIO('localhost', 9090)


def on_message(*args):
    print("Incoming msg: %s" % args)

io.on('message', on_message)

io.emit('hello_from_client')

while True:
    io.wait(seconds=0.1)

