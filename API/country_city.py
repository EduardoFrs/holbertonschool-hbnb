#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import geonamescache
from datetime import datetime

app = Flask(__name__)

""" initialise api with flask restx """
api = Api(app, version='1.0', title='Hbnb city and country API Lucas & Eduardo', description='API for manage cities and coutries')

""" namespace for city and country endpoint """
ns = api.namespace('city_country', description='manage interaction for city and country')

"""import preloaded countries """
gc = geonamescache.GeonamesCache()
countries = {country['iso']: country['name'] for country in gc.get_countries().values()}

"""data model for countries and cities """
country_model = api.model('Country', {
    'name': fields.String(required=True, description='Country name'),
    'code': fields.String(required=True, description='Country code (ISO 3166-1 alpha-2)')
})

city_model = api.model('City', {
    'id': fields.Integer(readonly=True, description='City id'),
    'name': fields.String(required=True, description='City name'),
    'country_code': fields.String(required=True, description='Country code (ISO 3166-1 alpha-2)'),
    'created_at': fields.DateTime(readonly=True, description='Creation timestamp'),
    'updated_at': fields.DateTime(readonly=True, description='Last update timestamp')
})

"""list for all cities"""
cities = []
city_id_counter = 1


def get_country_name(code):
    return countries.get(code)

def get_city_index(city_id):
    for i, city in enumerate(cities):
        if city['id'] == city_id:
            return i
    return -1

def validate_city_data(data):
    errors = []
    if 'name' not in data:
        errors.append('City name is required')
    if 'country_code' not in data:
        errors.append('Country code is required')
    elif data['country_code'] not in countries:
        errors.append('Invalid country code')
    elif any(city['name'] == data['name'] and city['country_code'] == data['country_code'] for city in cities):
        errors.append('City with the same name already exists in the country')
    return errors


@ns.route('/countries')
class CountryList(Resource):
    @ns.doc('list_countries')
    @ns.marshal_list_with(country_model)
    def get(self):
        """get list of all countries"""
        return [{'name': name, 'code': code} for code, name in countries.items()]

@ns.route('/countries/<country_code>')
@ns.response(404, 'Country not found')
@ns.param('country_code', 'the code of the country')
class CountryDetails(Resource):
    @ns.doc('get_country')
    @ns.marshal_with(country_model)
    def get(self, country_code):
        """get details of a specific country by is code"""
        country_name = get_country_name(country_code)
        if country_name:
            return {'name': country_name, 'code': country_code}
        else:
            api.abort(404, "Country not found")

@ns.route('/countries/<country_code>/cities')
@ns.response(404, 'Country not found')
@ns.param('country_code', 'the code of the country')
class CountryCities(Resource):
    @ns.doc('get_country_cities')
    @ns.marshal_list_with(city_model)
    def get(self, country_code):
        """get all cities of a country"""
        if country_code not in countries:
            api.abort(404, "Country not found")
        return [city for city in cities if city['country_code'] == country_code]

@ns.route('/cities')
class CityList(Resource):
    @ns.doc('list_cities')
    @ns.marshal_list_with(city_model)
    def get(self):
        """list of all cities"""
        return cities

    @ns.doc('create_city')
    @ns.expect(city_model)
    @ns.marshal_with(city_model, code=201)
    def post(self):
        """create a new city"""
        global city_id_counter
        data = request.json
        errors = validate_city_data(data)
        if errors:
            api.abort(400, ", ".join(errors))

        new_city = {
            'id': city_id_counter,
            'name': data['name'],
            'country_code': data['country_code'],
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        cities.append(new_city)
        city_id_counter += 1
        return new_city, 201

@ns.route('/cities/<city_id>')
@ns.response(404, 'City not found')
@ns.param('city_id', 'The city id')
class CityDetails(Resource):
    @ns.doc('get_city')
    @ns.marshal_with(city_model)
    def get(self, city_id):
        """get details of a specific city"""
        city_index = get_city_index(city_id)
        if city_index >= 0:
            return cities[city_index]
        else:
            api.abort(404, "City not found")

    @ns.doc('update_city')
    @ns.expect(city_model)
    @ns.marshal_with(city_model)
    def put(self, city_id):
        """ update an existing city """
        city_index = get_city_index(city_id)
        if city_index >= 0:
            data = request.json
            errors = validate_city_data(data)
            if errors:
                api.abort(400, ", ".join(errors))
            cities[city_index].update({
                'name': data['name'],
                'country_code': data['country_code'],
                'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            return cities[city_index]
        else:
            api.abort(404, "City not found")

    @ns.doc('delete_city')
    @ns.response(204, 'City deleted')
    def delete(self, city_id):
        """delete a specific city"""
        global cities
        city_index = get_city_index(city_id)
        if city_index >= 0:
            del cities[city_index]
            return '', 204
        else:
            api.abort(404, "City not found")

if __name__ == "__main__":
    app.run()
