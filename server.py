import flask
from flask_socketio import SocketIO, emit

from time import sleep

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
io = SocketIO(app)


@io.on('connect')
def test_connect():
    print("Client connected")
    for i in range(3):
        emit('message', {'data': str(i)})
        sleep(1)

if __name__ == '__main__':
    io.run(app, port=9090, debug=True)