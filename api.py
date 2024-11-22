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
