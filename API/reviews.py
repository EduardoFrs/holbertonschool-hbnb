#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, Namespace, fields, abort
from datetime import datetime
import uuid

api = Namespace('reviews', description='Review operations')

""" Sample data for storing reviews """
reviews = []

""" data model for reviews """
review_model = api.model('Review', {
    'id': fields.String(readonly=True, description='review unique id'),
    'place_id': fields.String(required=True, description='place unique id'),
    'user_id': fields.String(required=True, description='user unique id'),
    'rating': fields.Integer(required=True, description='rating of the place'),
    'comment': fields.String(required=True, description='comment on the place'),
    'created_at': fields.DateTime(readonly=True, description='review creation timestamp'),
    'updated_at': fields.DateTime(readonly=True, description='review latest update timestamp')
})

def get_review_index(review_id):
    for i, review in enumerate(reviews):
        if review['id'] == review_id:
            return i
    return -1

def validate_review_data(data):
    errors = []
    if 'user_id' not in data or 'place_id' not in data or 'rating' not in data or 'comment' not in data:
        errors.append('Missing required fields')
    else:
        if data['user_id'] not in ['user1', 'user2', 'user3']:
            errors.append('Invalid user ID')
        if data['place_id'] not in ['place1', 'place2', 'place3']:
            errors.append('Invalid place ID')
        if not (1 <= data['rating'] <= 5):
            errors.append('Rating must be between 1 and 5')
    return errors

@api.route('/<review_id>')
@api.response(404, 'Review not found')
@api.param('review_id', 'The review id')
class Review(Resource):
    @api.doc('get_review')
    @api.marshal_with(review_model)
    def get(self, review_id):
        """ Get details of a specific review """
        review_index = get_review_index(review_id)
        if review_index >= 0:
            return reviews[review_index]
        else:
            api.abort(404, "Review not found")

    @api.doc('update_review')
    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """ Update an existing review """
        review_index = get_review_index(review_id)
        if review_index >= 0:
            data = request.json
            errors = validate_review_data(data)
            if errors:
                api.abort(400, ", ".join(errors))
            reviews[review_index].update({
                'place_id': data['place_id'],
                'user_id': data['user_id'],
                'rating': data['rating'],
                'comment': data['comment'],
                'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            return reviews[review_index]
        else:
            api.abort(404, "Review not found")

    @api.doc('delete_review')
    @api.response(204, 'Review deleted')
    def delete(self, review_id):
        """ Delete a specific review """
        global reviews
        review_index = get_review_index(review_id)
        if review_index >= 0:
            del reviews[review_index]
            return '', 204
        else:
            api.abort(404, "Review not found")

@api.route('/places/<place_id>/reviews')
@api.param('place_id', 'The place id')
class PlaceReviewList(Resource):
    @api.doc('create_place_review')
    @api.expect(review_model)
    @api.marshal_with(review_model, code=201)
    def post(self, place_id):
        """ Create a new review for a specified place """
        data = request.json
        data['place_id'] = place_id
        errors = validate_review_data(data)
        if errors:
            api.abort(400, ", ".join(errors))

        new_review = {
            'id': str(uuid.uuid4()),
            'place_id': data['place_id'],
            'user_id': data['user_id'],
            'rating': data['rating'],
            'comment': data['comment'],
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        reviews.append(new_review)
        return new_review, 201

@api.route('/users/<user_id>/reviews')
@api.param('user_id', 'The user id')
class UserReviewList(Resource):
    @api.doc('get_user_reviews')
    @api.marshal_list_with(review_model)
    def get(self, user_id):
        """ Retrieve all reviews written by a specific user """
        user_reviews = [review for review in reviews if review['user_id'] == user_id]
        return user_reviews

@api.route('/places/<place_id>/reviews')
@api.param('place_id', 'The place id')
class PlaceReviewList(Resource):
    @api.doc('get_place_reviews')
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """ Retrieve all reviews for a specific place """
        place_reviews = [review for review in reviews if review['place_id'] == place_id]
        return place_reviews
