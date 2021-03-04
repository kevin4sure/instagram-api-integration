import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/welcome", methods=["GET"])
def index():
    return jsonify(msg="hello world!")


port = int(os.getenv("PORT", 0))
if __name__ == '__main__':
    if port != 0:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True)    