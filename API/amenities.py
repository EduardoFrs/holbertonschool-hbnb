from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime
import uuid


app = Flask(__name__)

""" initialise api with flask restx """
api = Api(app, version='1.0', title='Hbnb amenities API Lucas & Eduardo', description='API for manage amenities')

""" namespace for amenities endpoints """
ns = api.namespace('amenities', description='manage amenities operations')


""" data model for amenities """
amenities_model = api.model('amenity', {
    'id': fields.String(readonly=True, description='amenity id'),
    'name': fields.String(required=True, description='name of the amenity'),
    'created_at': fields.String(readonly=True, description='amenity creation timestamp'),
    'updated_at': fields.String(readonly=True, description='amenity latest update timestamp')
})

""" list for store amenities """
amenities = []


@ns.route('/amenities')
class AmenityList(Resource):
    @ns.doc('list_amenities')
    @ns.marshal_list_with(amenities_model)
    def get(self):
        """get list of all amenities"""
        return amenities, 200

    @ns.doc('create_amenity')
    @ns.expect(amenities_model)
    @ns.marshal_list_with(amenities_model, code=201)
    def post(self):
        """create new amenity"""
        global next_id
        data = request.get_json()
        if 'name' not in data:
            api.abort(400, 'Name required')
        if any(amenity['name'] == data['name'] for amenity in amenities):
            api.abort(409, 'Amenity already exist')

        new_amenity = {
            'id': str(uuid.uuid4()),
            'name': data['name'],
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'uptaded_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        next_id += 1
        amenities.append(new_amenity)
        return new_amenity, 201

@ns.route('/amenities/<amenity_id>')
@ns.response(404, 'Amenity not found')
@ns.param('id', 'amenity id')
class Amenity(Resource):
    @ns.doc('get_amenity')
    @ns.marshal_with(amenities_model)
    def get(self, id):
        """get informations about specific amenity"""
        amenity = next((amenity for amenity in amenities if amenity['id'] == id), None)
        if amenity is None:
            api.abort(404, 'amenity not found')
        return amenity, 200

    @ns.doc('update_amenity')
    @ns.expect(amenities_model)
    @ns.marshal_with(amenities_model)
    def put(self, id):
        """update existing amenity"""
        data = request.get_json()
        amenity = next((amenity for amenity in amenities if amenity['id'] == id), None)
        if amenity is None:
            api.abort(404, 'amenity not found')
        if 'name' in data and data['name']:
            if any(amenity['name'] == data['name'] and amenity['id'] != id for amenity in amenities):
                api.abort(409, 'Amenity already exist')
            amenity['name'] = data['name']
        amenity['uptaded_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")
        return amenity, 200

    @ns.doc('delete_amenity')
    @ns.response(204, 'amenity deleted')
    def delete(self, id):
        """delete a specific amenity"""
        global amenities
        amenity = next((amenity for amenity in amenities if amenity['id'] == id), None)
        if amenity is None:
            api.abort(404, "amenity not found")

        amenities = [amenity for amenity in amenities if amenity['id'] != id]
        return '', 204

if __name__ == '__main__':
    app.run()
