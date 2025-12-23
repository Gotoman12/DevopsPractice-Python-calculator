from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/add")
def add_api():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(result=add(a, b))

@app.route("/subtract")
def subtract_api():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(result=subtract(a, b))

@app.route("/multiply")
def multiply_api():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(result=multiply(a, b))

@app.route("/divide")
def divide_api():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify(result=divide(a, b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
