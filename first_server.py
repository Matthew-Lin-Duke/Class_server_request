from flask import Flask, jsonify, request

app = Flask(__name__)

name_database = []


@app.route("/", methods=["GET"])
def server_on():
    return "Server On"


@app.route("/info", methods=["GET"])
def info():
    info_dic = {
        "author": "Matthew Lin",
        "version": 2.0,
        "data": "March 30, 2020"
    }
    return jsonify(info_dic)


@app.route("/number", methods=["GET"])
def return_number():
    return jsonify(5)


@app.route("/send_name", methods=["POST"])
def add_name_to_database():
    name_to_add = request.get_json()
    name_database.append(name_to_add)
    return "Name {} added".format(name_to_add)


@app.route("/get_names", methods=["GET"])
def get_names():
    return jsonify(name_database)


if __name__ == "__main__":
    app.run()
