from flask import request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from flask_restful import Resource

from schemas.basic import BasicSchema
from models.active import ActiveModel
from models.basic import (
    ERROR_WRITING_BASIC_TABLE
)

basic_schema = BasicSchema()

UPDATE_SUCCESSFUL = 'Update successful.'
UPDATE_UNSUCCESSFUL = 'Update unsuccessful.'
INVALID_REQUEST = 'Invalid request.'


class Profile(Resource):
    # For updating profile
    @jwt_required
    def put(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Create an object using request data
        fresh_basic_object = basic_schema.load(request.get_json())
        # Creating an for the requesting active user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Check if basic data already exists
        existing_basic_object = active_user_object.basic
        if not existing_basic_object:
            fresh_basic_object.uid = current_user
            if fresh_basic_object.create_entry() == ERROR_WRITING_BASIC_TABLE:
                return {'message': UPDATE_UNSUCCESSFUL}
            return {'message': UPDATE_SUCCESSFUL}
        else: 
            # Update all fields with new data
            existing_basic_object.bio = fresh_basic_object.bio
            existing_basic_object.dob = fresh_basic_object.dob
            existing_basic_object.country = fresh_basic_object.country
            existing_basic_object.profession = fresh_basic_object.profession
            existing_basic_object.image = fresh_basic_object.image
            if existing_basic_object.create_entry() == ERROR_WRITING_BASIC_TABLE:
                return {'message': UPDATE_UNSUCCESSFUL}
            return {'message': UPDATE_SUCCESSFUL}







