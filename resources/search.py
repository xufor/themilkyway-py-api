from flask import request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from flask_restful import Resource

from models.active import ActiveModel
from schemas.search import SearchSchema

search_schema = SearchSchema()

NO_IMAGE_AVAILABLE = 'No Image available'


class Search(Resource):
    @jwt_required
    def post(self):
        # Get the current user
        current_user = get_jwt_identity()
        # Parse incoming data and extract required field
        search_data = search_schema.load(request.get_json())
        incoming_name = search_data['name']
        incoming_version = search_data['version']
        # Creating an list of objects for the requesting active user
        active_user_objects = ActiveModel.find_entry_by_name(incoming_name, incoming_version)
        # Remove the result which is same as the requesting user
        for user in active_user_objects:
            if user.uid == current_user:
                active_user_objects.remove(user)
        # Return results and if there are no favourites then empty list is returned
        return {'results': [
            {
                'uid': user.uid,
                'name': user.name,
                'image': user.basic.image if user.basic is not None else NO_IMAGE_AVAILABLE
            }
            for user in active_user_objects],
            'final': len(active_user_objects) <= incoming_version * 15
        }
