from flask import Flask, jsonify, request

db = []

app = Flask(__name__)


def add_patient_to_db(name, id, age):
    new_patient = {"name": name,
                   "id": id,
                   "age": age}
    db.append(new_patient)
    return True


def init_database():
    add_patient_to_db("David Ward", 101, 60)
    add_patient_to_db("Bill Gates", 123, 65)
    # Add code to start logging



if __name__ == '__main__':
    init_database()
    app.run()
