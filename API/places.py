from flask import Flask, request, jsonify, abort
from flask_restx import Api, Namespace, Resource, fields
from datetime import datetime
import uuid

api = Namespace('places', description='Places operations')

""" data model for places """
place_model = api.model('Place', {
    'id': fields.String(readonly=True, description='The unique identifier of the place'),
    'name': fields.String(required=True, description='Name of the place'),
    'description': fields.String(required=True, description='Description of the place'),
    'address': fields.String(required=True, description='Address of the place'),
    'city_id': fields.Integer(required=True, description='ID of the city of the place'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'host_id': fields.Integer(required=True, description='ID of the host of the place'),
    'number_of_rooms': fields.Integer(required=True, description='Number of rooms in the place'),
    'number_of_bathrooms': fields.Integer(required=True, description='Number of bathrooms in the place'),
    'price_per_night': fields.Float(required=True, description='Price per night in the place'),
    'max_guests': fields.Integer(required=True, description='Maximum number of guests in the place'),
    'amenity_ids': fields.List(fields.String, required=True, description='List of amenity IDs of the place'),
    'created_at': fields.DateTime(readonly=True, description='The date and time the place was created'),
    'updated_at': fields.DateTime(readonly=True, description='The date and time the place was last updated')
})

"""list for storing all places"""
places = {}

"""function to validate geographical coordinates"""
def validate_coordinates(latitude, longitude):
    if not (-90 <= latitude <= 90):
        abort(400, "Invalid latitude, must be between -90 and 90")
    if not (-180 <= longitude <= 180):
        abort(400, "Invalid longitude, must be between -180 and 180")

"""function to validate the city"""
def validate_city(city_id):
    if city_id not in cities:
        abort(400, "Invalid city_id")

"""function to validate amenities"""
def validate_amenities(amenity_ids):
    for amenity_id in amenity_ids:
        if amenity_id not in amenities:
            abort(400, f"Amenity ID does not exist: {amenity_id}")

@api.route('/')
class PlaceList(Resource):
    @api.doc('list_places')
    @api.marshal_list_with(place_model)
    def get(self):
        """Retrieve a list of all places"""
        return list(places.values()), 200

    @api.doc('create_place')
    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    def post(self):
        """Create a new place"""
        data = request.get_json()
        validate_coordinates(data['latitude'], data['longitude'])
        validate_city(data['city_id'])
        validate_amenities(data['amenity_ids'])
        if data['number_of_rooms'] < 0 or data['number_of_bathrooms'] < 0 or data['max_guests'] < 0:
            abort(400, "Number of rooms, bathrooms, and max guests must be non-negative")
        place_id = str(uuid.uuid4())
        data['id'] = place_id
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        places[place_id] = data
        return data, 201

@api.route('/<string:id>')
@api.response(404, 'Place not found')
class Place(Resource):
    @api.doc('get_place')
    @api.marshal_with(place_model)
    def get(self, id):
        """Retrieve detailed information about a specific place"""
        if id not in places:
            abort(404, "Place not found")
        return places[id], 200

    @api.doc('update_place')
    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, id):
        """Update an existing place’s information"""
        if id not in places:
            abort(404, "Place not found")
        data = request.get_json()
        validate_coordinates(data['latitude'], data['longitude'])
        validate_city(data['city_id'])
        validate_amenities(data['amenity_ids'])
        if data['number_of_rooms'] < 0 or data['number_of_bathrooms'] < 0 or data['max_guests'] < 0:
            abort(400, "Number of rooms, bathrooms, and max guests must be non-negative")
        data['updated_at'] = datetime.utcnow()
        places[id].update(data)
        return places[id], 200

    @api.doc('delete_place')
    @api.response(204, 'Place deleted')
    def delete(self, id):
        """Delete a specific place"""
        if id not in places:
            abort(404, "Place not found")
        del places[id]
        return '', 204