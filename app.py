import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/welcome", methods=["GET"])
def index():
    return jsonify(msg="hello world!")


@app.route("/auth", methods=["GET", "POST"])
def authenticate():
    reqData =  json.loads(request.data)
    return jsonify(reqData)  


port = int(os.getenv("PORT", 0))
if __name__ == '__main__':
    if port != 0:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True, port=8080)    