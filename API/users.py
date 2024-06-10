#!/usr/bin/python3
from flask import Flask, request, jsonify
from datetime import datetime
from validate_email import validate_email

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

    """ verify valid inputs """
    if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    """ verify valid email """
    if not validate_email(data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    """ verify unique email """
    if any(user['email'] == data['email'] for user in users):
        return jsonify({"error": "Email already exist"}), 409

    """ verify non-empty first name and last name """
    if data['first_name'] == '' or data['last_name'] == '':
        return jsonify({"error": "First name and Last name cannot be empty"}), 400

    new_user = {
        "id": len(users) + 1,
        "email": data['email'],
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
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
    return jsonify({"error": "User not found"}), 404

""" update an existing user """
@app.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        user.update({
            "email": data['email'],
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

""" delete a user """
@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        users = [user for user in users if user["id"] != user_id]
        return '', 204
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()