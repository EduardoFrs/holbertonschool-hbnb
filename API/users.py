#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime
from validate_email import validate_email

# CHANGEMENT TEST POUR CHECK SI BRANCH OK __

app = Flask(__name__)

""" initialise api with flask restx """
api = Api(app, version='1.0', title='Hbnb users API Lucas & Eduardo', description='API for manage users')

""" namespace for users endpoints """
ns = api.namespace('users', description='user operations')

""" data model for users """
user_model = api.model('user', {
    'id': fields.Integer(readonly=True, description='unique user id'),
    'email': fields.String(required=True, description='user email adress'),
    'first_name': fields.String(required=True, description='user first name'),
    'last_name': fields.String(required=True, description='user last name'),
    'created_at': fields.DateTime(readonly=True, description='user creation timestamp'),
    'updated_at': fields.DateTime(readonly=True, description='user latest update timestamp')
})

""" list for store all users """
users = []


""" class for manage the list of users """


@ns.route('/users')
class Userlist(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """get list of all users"""
        return users

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_list_with(user_model, code=201)
    def post(self):
        """create a new user"""
        data = request.get_json()

        """ verify valid inputs """
        if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
            api.abort(400, "Missing required fields")

        """ verify valid email """
        if not validate_email(data['email']):
            api.abort(400, "Invalid email format")

        """ verify unique email """
        if any(user['email'] == data['email'] for user in users):
            api.abort(409, "Email already exist")

        """ verify non-empty first name and last name """
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


""" class for manage a specific user """


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
    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, user_id):
        """ update an existing user """
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
    def delete(self, user_id):
        """Delete a user given its identifier"""
        global users
        users = [user for user in users if user["id"] != user_id]
        return '', 204


if __name__ == "__main__":
    app.run()
