import time
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from db import db
from schemas.story import StorySchema
from schemas.edit import EditSchema
from resources.profile import genres
from models.stories import (
    StoryModel,
    ERROR_WRITING_STORY_TABLE
)

story_schema = StorySchema()
edit_schema = EditSchema()

ERROR_SUBMITTING_STORY = 'Error in submitting story.'
STORY_SUCCESSFULLY_SUBMITTED = 'Story successfully submitted.'
STORY_SUCCESSFULLY_UPDATED = 'Story successfully updated.'
INVALID_GENRE = 'The provided genres are not valid.'
INVALID_REQUEST = 'Invalid request.'
SUMMARY_TOO_LONG = 'Summary cannot be greater than length of 80 words.'
STORY_TOO_LONG = 'Story cannot be greater than length of 10000 words.'
TITLE_TOO_LONG = 'Title cannot be greater than length of 10 words.'


class Submit(Resource):
    # This method only requires story and summary as json
    @jwt_required
    def post(self):
        # Loaded incoming data into story
        story_object = story_schema.load(request.get_json(), db.session)
        # Check if the the genres is valid or not
        # Accepts 3 genres only
        genre_list = story_object.genre.split(',')
        if not (len(genre_list) <= 3 and set(genre_list).issubset(set(genres))):
            return {'message': INVALID_GENRE}
        # Check word length of various elements
        if StoryModel.words_counter(story_object.title) > 10:
            return {'message': TITLE_TOO_LONG}
        if StoryModel.words_counter(story_object.summary) > 80:
            return {'message': SUMMARY_TOO_LONG}
        if StoryModel.words_counter(story_object.story) > 10000:
            return {'message': STORY_TOO_LONG}
        # Adding time, uid and sid fields to story object
        story_object.time = time.asctime(time.localtime(time.time()))
        story_object.uid = get_jwt_identity()
        story_object.sid = StoryModel.generate_fresh_sid()
        story_object.status = 'unapproved'
        story_object.views = 0
        story_object.likes = 0
        # Creating a new entry in story table and checking for success
        if story_object.create_story() == ERROR_WRITING_STORY_TABLE:
            return {'message': ERROR_SUBMITTING_STORY}, 500
        return {'message': STORY_SUCCESSFULLY_SUBMITTED}, 201

    @jwt_required
    def put(self):
        # Loaded incoming data into dict
        story_data = edit_schema.load(request.get_json())
        # Find the target story
        discovered_story = StoryModel.find_story_by_sid(story_data['sid'])
        # First check existence and then check for valid status
        if (discovered_story is None) or (not StoryModel.check_story_status(discovered_story)):
            return {'message': INVALID_REQUEST}, 400
        else:
            discovered_story.story = story_data['story']
            discovered_story.summary = story_data['summary']
            discovered_story.title = story_data['title']
            discovered_story.genre = story_data['genre']
            if discovered_story.create_story() == ERROR_WRITING_STORY_TABLE:
                return {'message': ERROR_SUBMITTING_STORY}, 500
        return {'message': STORY_SUCCESSFULLY_UPDATED}, 200














