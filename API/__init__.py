#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

""" list for store all users """
users = []

@app.route("/")
def home():
    return "HBnb Lucas & Eduardo!"

""" create a new user """
@app.route("/users", methods=['POST'])
def create_new_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "email": data['email'],
        "first_name": data['first_name'],
        "last_name": data['last_name']
    }
    users.append(new_user)
    return jsonify(new_user), 201

""" get list of all users """
@app.route("/users", methods=['GET'])
def list_users():
    return jsonify(users), 200


""" get details of a specific user """
@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"User not found"}), 404

""" update an existing user """
@app.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        user.update({
            "email": data['email'],
             "first_name": data['first_name'],
            "last_name": data['last_name']
        })
        return jsonify(user), 200
    return jsonify({"User not found"}), 404

""" delete a user """
@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        users = [user for user in users if user["id"] != user_id]
        return '', 204
    return jsonify({"User not found"}), 404

if __name__ == "__main__":
    app.run()