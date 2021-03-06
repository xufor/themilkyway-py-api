from flask import request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from flask_restful import Resource

from models.active import ActiveModel
from schemas.search import SearchSchema
from models.stories import StoryModel

search_schema = SearchSchema()

NO_IMAGE_AVAILABLE = 'No Image available.'
NO_MORE_SEARCH_DATA = 'No more search data available.'


class Search(Resource):
    @jwt_required
    def post(self):
        # Get the current user
        current_user = get_jwt_identity()
        # Parse incoming data and extract required field
        search_data = search_schema.load(request.get_json())
        incoming_string = search_data['string']
        incoming_version = search_data['version']
        incoming_content = search_data['content']

        if incoming_content == 'authors':
            active_user_objects = ActiveModel.find_entry_by_name(incoming_string, incoming_version, current_user)
            # Slice the results according to the need
            if incoming_version > 1:
                active_user_objects = active_user_objects[(incoming_version-1)*15:]
            # Return results and if there are no users matching the criteria then return empty list
            # Return empty list if there are no more versions with users matching the criteria
            if len(active_user_objects) != 0:
                return {'results': ActiveModel.generate_search_data(active_user_objects, current_user)}
            else:
                return {'message': NO_MORE_SEARCH_DATA}, 400

        elif incoming_content == 'stories':
            discovered_story_objects = StoryModel.find_stories_by_title(incoming_string, incoming_version)
            # Slice the results according to the need
            if incoming_version > 1:
                discovered_story_objects = discovered_story_objects[(incoming_version - 1)*15:]
            # Return results and if there are no users matching the criteria then return empty list
            # Return empty list if there are no more versions with users matching the criteria
            if len(discovered_story_objects) != 0:
                return {'results': [StoryModel.generate_story_element_data(story) for story in discovered_story_objects]}
            else:
                return {'message': NO_MORE_SEARCH_DATA}, 400
