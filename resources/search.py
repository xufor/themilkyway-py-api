from flask import request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from flask_restful import Resource

from models.active import ActiveModel
from schemas.search import SearchSchema

search_schema = SearchSchema()

NO_IMAGE_AVAILABLE = 'No Image available.'


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
        # Slice the results according to the need
        if incoming_version > 1:
            active_user_objects = active_user_objects[(incoming_version-1)*15:]
        # Return results and if there are no users matching the criteria then return empty list
        # Return empty list if there are no more versions with users matching the criteria
        return {'results': [
            {
                'uid': user.uid,
                'name': user.name,
                'image': user.basic.image if (user.basic and user.basic.image is not 'no-image') else NO_IMAGE_AVAILABLE
            }
            for user in active_user_objects]
        }
