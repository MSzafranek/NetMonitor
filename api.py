from flask import Flask, jsonify
from db_module import get_ping_stats

app = Flask(__name__)

@app.route("/api/stats")
def stats():
    return jsonify(get_ping_stats())

if __name__ == "__main__":
    app.run(debug=True)
