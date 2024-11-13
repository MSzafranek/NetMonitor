#ping_module.py
from ping3 import ping
import time
import sqlite3
import click

def ping_addresses():
    targets = {"internet": "8.8.8.8", "gateway": "192.168.1.1"}
    results = {}

    for target_name, address in targets.items():
        response_time = ping(address)
        results[target_name] = response_time if response_time is not None else -1

    return results

#db_module.py
import sqlite3
from datetime import datetime

def init_db(db_module=None):
    conn = sqlite3.connect("network_monitor.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            response_time REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP 
                   )
""")
    conn.commit()
    conn.close()



def save_ping_result(target, response_time):
    conn = sqlite3.connect("network_monitor.db")
    c = conn.cursor()
    c.execute("INSERT INTO pings (target, response_time) VALUES (?, ?)", (target, response_time))
    conn.commit()
    conn.close()
#monitor.py
import time
from ping_module import ping_addresses
from db_module import save_ping_result, init_db

def monitor_network(interval=60):
    init_db()
    while True:
        results = ping_addresses()
        for target, response_time in results.items():
            save_ping_result(target, response_time)
        time.sleep(interval)

#api.py
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_ping_stats():
    conn = sqlite3.connect("network_monitor.db")
    c = conn.cursor()
    c.execute("SELECT target, AVG(response_time) AS avg_time, MIN(response_time) AS min_time, MAX(response_time) AS max_time FROM pings GROUP BY target")
    data = c.fetchall()
    conn.close()
    return [{"target": row[0], "avg_time": row[1], "min_time": row[2], "max_time": row[3]} for row in data]

@app.route("/api/stats")
def stats():
    return jsonify(get_ping_stats())

if __name__ == "__main__":
    app.run(debug=True)
    # app.py
    from flask import Flask, render_template
    from flask_socketio import SocketIO
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


    def update_stats():
        while True:
            time.sleep(60)  #Aktualizowanie co minutę
            stats = get_ping_stats()
            socketio.emit("update_stats", stats)


    if __name__ == "__main__":
        socketio.run(app)

