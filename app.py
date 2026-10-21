import os

from flask import Flask, jsonify, request

from factorial import factorial

MAX_NUMBER = 1000

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Factorial app", usage="/factorial?number=5")


@app.route("/factorial")
def get_factorial():
    raw = request.args.get("number")
    if raw is None:
        return jsonify(error="query parameter 'number' is required"), 400
    try:
        number = int(raw)
    except ValueError:
        return jsonify(error="number must be an integer"), 400
    if number < 0:
        return jsonify(error="number must be non-negative"), 400
    if number > MAX_NUMBER:
        return jsonify(error=f"number must not exceed {MAX_NUMBER}"), 400
    return jsonify(number=number, factorial=factorial(number))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))