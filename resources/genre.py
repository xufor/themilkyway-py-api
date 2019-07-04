from flask import request
from flask_jwt_extended import (
    jwt_required
)
from flask_restful import Resource

from schemas.genre import GenreSchema
from models.stories import StoryModel


genre_schema = GenreSchema()

NO_MORE_GENRE_DATA = 'No more genre data available.'


# An algorithm that filters duplicates
def return_unique_list(object_list):
    filtered_list = []
    for story in object_list:
        if story.uid not in [uid for uid in filtered_list]:
            filtered_list.append(story)
    return filtered_list


class Genre(Resource):
    @jwt_required
    def post(self):
        genre_data = genre_schema.load(request.get_json())
        discovered_stories = StoryModel.find_stories_by_genre(genre_data['genre'], genre_data['version'])
        # Slice the results based on version
        if genre_data['version'] > 1:
            discovered_stories = discovered_stories[(genre_data['version'] - 1) * 15:]
        # Remove duplicates
        discovered_stories = return_unique_list(discovered_stories)
        # Send appropriate response
        if len(discovered_stories) != 0:
            return {'results': [StoryModel.generate_story_element_data(story) for story in discovered_stories]}
        else:
            return {'message': NO_MORE_GENRE_DATA}, 400





