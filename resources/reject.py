from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_claims
)

from models.stories import StoryModel
from schemas.approve import ApproveSchema

approve_schema = ApproveSchema()

REJECTED_SUCCESSFULLY = 'Story successfully rejected.'
INVALID_STORY_IDENTITY = 'No such story exists.'


class Reject(Resource):
    # This method only requires story and summary as json
    @jwt_required
    def put(self):
        claims = get_jwt_claims()
        # Will ensure admin privileges
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}
        # Parse incoming data using schema
        parsed_data = approve_schema.load(request.get_json())
        # Get the story to be approved from story table and check existence
        discovered_story = StoryModel.find_entry_by_sid(parsed_data['sid'])
        if discovered_story is None:
            return {'message': INVALID_STORY_IDENTITY}
        # Run create_story function to reflect changes
        discovered_story.delete_story()
        # Send a success message
        return {'message': REJECTED_SUCCESSFULLY}, 202
