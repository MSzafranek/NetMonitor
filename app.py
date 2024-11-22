from flask import Flask, render_template
from ping_module import ping_addresses
from db_module import init_db
import time
import threading

app = Flask(__name__)

ping_data = [{"target": "internet", "response_time": -1, "timestamp": "Initializing..."},
             {"target": "gateway", "response_time": -1, "timestamp": "Initializing..."}]


def monitor_network(interval=60):
    global ping_data
    while True:
        results = ping_addresses()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        ping_data = [
            {"target": target, "response_time": response_time, "timestamp": timestamp}
            for target, response_time in results.items()
        ]
        time.sleep(interval)

@app.route("/")
def index():
    return render_template("report.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/api/stats")
def stats():
    return jsonify(get_ping_stats())

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=monitor_network, daemon=True)
    monitor_thread.start()
    app.run(debug=True, host='0.0.0.0', port=5000))
