import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from flask import Flask, render_template, jsonify
from ping_module import ping_addresses
from db_module import init_db, get_ping_stats
import time
import threading

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("report.html")

@app.route("/api/stats")
def stats():
    return jsonify(get_ping_stats())

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=monitor_network, daemon=True)
    monitor_thread.start()
    app.run(debug=True, host='0.0.0.0', port=5000)
