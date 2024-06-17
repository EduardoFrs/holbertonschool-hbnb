from flask_restx import Api, Resource, reqparse
from ..Model import user

api = Api()

class UserResource(Resource):
    def __init__(self, user_manager):
        pass

