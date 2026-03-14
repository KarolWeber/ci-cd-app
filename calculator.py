from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a + b)

@app.route("/sub")
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a - b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)