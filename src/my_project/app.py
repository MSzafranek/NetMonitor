import sys
from pathlib import Path

from NetMonitor.monitor import monitor_network


sys.path.append(str(Path(__file__).parent))
import threading

from db_module import get_ping_stats
from flask import Flask, jsonify, render_template, Response


app = Flask(__name__)


@app.route('/')
def _index() -> str:
    return render_template('report.html')


@app.route('/api/stats')
def _stats() -> Response:
    return jsonify(get_ping_stats())


if __name__ == '__main__':
    monitor_thread = threading.Thread(target=monitor_network, daemon=True)
    monitor_thread.start()
    app.run(debug=True, host='0.0.0.0', port=5000)  # noqa: S104, S201
