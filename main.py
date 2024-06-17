from flask import Flask
from flask_restx import Api


from API.users import api as users_api
from API.country_city import api as country_city_api
from API.places import api as places_api
from API.amenities import api as amenety_api
from API.reviews import api as review_api


app = Flask(__name__)

api = Api(app, version='1.0', title='Hbnb main API Lucas & Eduardo', description='main API')


api.add_namespace(users_api)
api.add_namespace(country_city_api)
api.add_namespace(places_api)
api.add_namespace(amenety_api)
api.add_namespace(review_api)


if __name__ == "__main__":
    app.run()

