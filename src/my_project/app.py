import sys
from pathlib import Path

from my_project.monitor import monitor_network


sys.path.append(str(Path(__file__).parent))
import threading

from flask import Flask, jsonify, render_template, Response

from my_project.db_module import get_ping_stats


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
