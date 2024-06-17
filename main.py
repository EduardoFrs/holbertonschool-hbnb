from flask import Flask
from flask_restx import Api


app = Flask(__name__)
api = Api(
    app,
    version='1.4.2.5.2.0 beta release fuck',
    title='HBNB PART. 1: Users API.',
    description='API to manage user endpoints. Sign off bro'
)


api.add_namespace(countryAPI)
api.add_namespace(cityAPI)
api.add_namespace(placeAPI)
api.add_namespace(userAPI)

api.init_app(app)

app.run(debug=True)