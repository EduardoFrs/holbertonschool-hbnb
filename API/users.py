#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, reqparse
from datetime import datetime
from validate_email import validate_email
from Model.user import User
from Model.base_model import BaseModel
from dataclasses import dataclass

# CHANGEMENT TEST POUR CHECK SI BRANCH OK __

app = Flask(__name__)
api = Api(
    app,
    version='1.4.2.5.2.0 beta release fuck',
    title='HBNB PART. 1: Users API.',
    description='API to manage user endpoints. Sign off bro'
)

ns = api.namespace('users', description='USERS ENDPOINTS')
api.add_namespace(ns)


@ns.route('/users')
class Userlist(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(User)
    def get(self):

        return User

    @ns.doc('create_user')
    @ns.expect(User)
    @ns.marshal_list_with(User, code=201)
    def post(self):

        # create a new user
        data = request.get_json()

        # verify valid inputs
        if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
            api.abort(400, "Missing required fields")

        # verify valid email
        if not validate_email(data['email']):
            api.abort(400, "Invalid email format")

        # verify unique email
        if any(user['email'] == data['email'] for user in users):
            api.abort(409, "Email already exist")

        # verify non-empty first name and last name
        if data['first_name'] == '' or data['last_name'] == '':
            api.abort(400, "First name and Last name cannot be empty")

        new_user = {
            "id": len(users) + 1,
            "email": data['email'],
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        users.append(new_user)
        return new_user, 201


# class for manage a specific user


@ns.route('/user_id')
@ns.response(404, 'User not found')
@ns.param('user_id', 'The user id')
class User(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, user_id):
        """ get details of a specific user by is id """
        user = next((user for user in users if user["id"] == user_id), None)
        if user:
            return user
        api.abort(404, "User not found")

    @ns.doc('update_user')
    @ns.expect(User)
    @ns.marshal_with(User)
    def put(self, user_id):
        # update an existing user """
        data = request.get_json()
        user = next((user for user in users if user["id"] == user_id), None)
        if user:
            user.update({
                "email": data['email'],
                "first_name": data['first_name'],
                "last_name": data['last_name'],
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            return user
        api.abort(404, "User not found")

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
