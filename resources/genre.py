from flask import request
from flask_jwt_extended import (
    jwt_required
)
from flask_restful import Resource

from schemas.genre import GenreSchema
from models.stories import StoryModel


genre_schema = GenreSchema()


class Genre(Resource):
    @jwt_required
    def post(self):
        genre_data = genre_schema.load(request.get_json())
        discovered_stories = StoryModel.find_stories_by_genre(genre_data['genre'], genre_data['version'])
        return {
            'results': [StoryModel.generate_story_element_data(story) for story in discovered_stories]
        }






