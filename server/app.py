from flask import Flask, jsonify, request
from flask_cors import CORS
from subprocess import call

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

items = ["Apple", "Orange", "Lemon", "Strawberry"]
db_dict = {}


@app.route('/items', methods=['GET', 'POST'])
def items_route():
    if request.method == 'GET':
        return jsonify({
        'status': 'success',
        'items': items
        })

@app.route('/database', methods=['GET', 'POST'])
def database_route():
    if request.method == 'POST':
        if (request.get_json()["submitCue"] == True):
            user_name = request.get_json()["name"].lower()
            user_order = request.get_json()["itemsArr"]
            add_to_db(user_name, user_order)
    else:
        return jsonify({
            'status': 'success',
            'db': db_dict
        })

def add_to_db(user_name,  user_order):
    if user_name not in db_dict.keys():
        db_dict[user_name] = {"order": user_order}
    else:
        for i in range(len(db_dict[user_name]["order"])):
            if user_order[i]["val"] != 0:
                db_dict[user_name]["order"][i]["val"] += user_order[i]["val"]
if __name__ == '__main__':
    app.run()