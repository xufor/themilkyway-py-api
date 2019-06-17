import time
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from db import db
from schemas.story import StorySchema
from models.stories import (
    StoryModel,
    ERROR_WRITING_STORY_TABLE
)

story_schema = StorySchema()

ERROR_SUBMITTING_STORY = 'Error in submitting story.'
STORY_SUCCESSFULLY_SUBMITTED = 'Story successfully submitted.'


class Submit(Resource):
    # This method only requires story and summary as json
    @jwt_required
    def post(self):
        # Loaded incoming data into story
        story_object = story_schema.load(request.get_json(), db.session)
        # Adding time, uid and sid fields to story object
        story_object.time = time.asctime(time.localtime(time.time()))
        story_object.uid = get_jwt_identity()
        story_object.sid = StoryModel.generate_fresh_sid()
        story_object.status = 'unapproved'
        story_object.reads = 0
        story_object.likes = 0
        # Creating a new entry in story table and checking for success
        if story_object.create_story() == ERROR_WRITING_STORY_TABLE:
            return {
                       'message': ERROR_SUBMITTING_STORY,
                       'details': ERROR_WRITING_STORY_TABLE
            }, 500
        return {
                   'message': STORY_SUCCESSFULLY_SUBMITTED,
                   'sid': story_object.sid
        }, 201










