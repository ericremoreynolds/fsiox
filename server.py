import gevent
import gevent.monkey
gevent.monkey.patch_all()

from time import sleep

import flask
from flask_socketio import SocketIO, emit

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
io = SocketIO(app)

@io.on('connect')
def on_connect():
    print("Client connected")

@io.on('hello_from_client')
def on_hello_from_client():
    for i in range(3):
        emit('message', str(i))
        print("Sent %s" % i)
        sleep(1)

if __name__ == '__main__':
    io.run(app, port=9090, debug=True)