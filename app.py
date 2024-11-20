from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread
import time
from db_module import get_ping_stats

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("report.html")

@socketio.on("connect")
def handle_connect():
    stats = get_ping_stats()
    socketio.emit("update_stats", stats)

def background_update():
    while True:
        time.sleep(60)
        stats = get_ping_stats()
        socketio.emit("update_stats", stats)

if __name__ == "__main__":
    thread = Thread(target=background_update)
    thread.daemon = True
    thread.start()
    socketio.run(app)
