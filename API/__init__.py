from flask import Flask
from resources import api
from users import ns

def create_app():
    app = Flask(__name__)


    api.init_app(app)

    api.add_namespace(ns)

    return app