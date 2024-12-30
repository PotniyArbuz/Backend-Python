from flask import Flask, jsonify, request
from dotenv import dotenv_values

app = Flask(__name__)

@app.route("/")
def server_info():
    return "My server"

@app.route("/author")
def author():
    author = {
        "name": "Stas",
        "course": 3,
        "age": 21,
    }
    return jsonify(author)

def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return int(config["PORT"])
    return 5000

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})

if __name__ == "__main__":
    app.run(debug=True, port=get_port())

