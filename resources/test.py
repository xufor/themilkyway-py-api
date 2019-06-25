from flask_restful import Resource
from models.active import StoryModel


class Test(Resource):
    @classmethod
    def get(cls):
        x = StoryModel.find_feed_stories_by_genre('Classic', 1)
        return {'result': [StoryModel.generate_story_element_data(obj) for obj in x]}
