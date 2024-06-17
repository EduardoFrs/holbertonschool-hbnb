#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restx import Api, Namespace, Resource, fields
import geonamescache
from datetime import datetime
import uuid


api = Namespace('city_country', description='manage interaction for city and country')


"""import preloaded countries """
gc = geonamescache.GeonamesCache()
countries = {country['iso']: country['name'] for country in gc.get_countries().values()}

"""data model for countries and cities """
country_model = api.model('Country', {
    'name': fields.String(required=True, description='Country name'),
    'code': fields.String(required=True, description='Country code (ISO 3166-1 alpha-2)')
})

city_model = api.model('City', {
    'id': fields.String(readonly=True, description='City id'),
    'name': fields.String(required=True, description='City name'),
    'country_code': fields.String(required=True, description='Country code (ISO 3166-1 alpha-2)'),
    'created_at': fields.DateTime(readonly=True, description='Creation timestamp'),
    'updated_at': fields.DateTime(readonly=True, description='Last update timestamp')
})

"""list for all cities"""
cities = []


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


@api.route('/countries')
class CountryList(Resource):
    @api.doc('list_countries')
    @api.marshal_list_with(country_model)
    def get(self):
        """get list of all countries"""
        return [{'name': name, 'code': code} for code, name in countries.items()]

@api.route('/countries/<country_code>')
@api.response(404, 'Country not found')
@api.param('country_code', 'the code of the country')
class CountryDetails(Resource):
    @api.doc('get_country')
    @api.marshal_with(country_model)
    def get(self, country_code):
        """get details of a specific country by is code"""
        country_name = get_country_name(country_code)
        if country_name:
            return {'name': country_name, 'code': country_code}
        else:
            api.abort(404, "Country not found")

@api.route('/countries/<country_code>/cities')
@api.response(404, 'Country not found')
@api.param('country_code', 'the code of the country')
class CountryCities(Resource):
    @api.doc('get_country_cities')
    @api.marshal_list_with(city_model)
    def get(self, country_code):
        """get all cities of a country"""
        if country_code not in countries:
            api.abort(404, "Country not found")
        return [city for city in cities if city['country_code'] == country_code]

@api.route('/cities')
class CityList(Resource):
    @api.doc('list_cities')
    @api.marshal_list_with(city_model)
    def get(self):
        """list of all cities"""
        return cities

    @api.doc('create_city')
    @api.expect(city_model)
    @api.marshal_with(city_model, code=201)
    def post(self):
        """create a new city"""
        data = request.json
        errors = validate_city_data(data)
        if errors:
            api.abort(400, ", ".join(errors))

        new_city = {
            'id': str(uuid.uuid4()),
            'name': data['name'],
            'country_code': data['country_code'],
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        cities.append(new_city)
        return new_city, 201

@api.route('/cities/<city_id>')
@api.response(404, 'City not found')
@api.param('city_id', 'The city id')
class CityDetails(Resource):
    @api.doc('get_city')
    @api.marshal_with(city_model)
    def get(self, city_id):
        """get details of a specific city"""
        city_index = get_city_index(city_id)
        if city_index >= 0:
            return cities[city_index]
        else:
            api.abort(404, "City not found")

    @api.doc('update_city')
    @api.expect(city_model)
    @api.marshal_with(city_model)
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

    @api.doc('delete_city')
    @api.response(204, 'City deleted')
    def delete(self, city_id):
        """delete a specific city"""
        global cities
        city_index = get_city_index(city_id)
        if city_index >= 0:
            del cities[city_index]
            return '', 204
        else:
            api.abort(404, "City not found")