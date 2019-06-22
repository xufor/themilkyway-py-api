import time
from flask import request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from flask_restful import Resource

from schemas.like import LikeSchema
from models.stories import StoryModel
from models.active import ActiveModel
from models.like import (
    ERROR_WRITING_LIKE_TABLE,
    ERROR_DELETING_LIKE_TABLE
)

like_schema = LikeSchema()

CANNOT_LIKE_OWN_STORY = 'You cannot like your story.'
CANNOT_UNLIKE_OWN_STORY = 'You cannot remove like from your own story.'
LIKE_SUCCESSFUL = 'Like successful.'
LIKE_UNSUCCESSFUL = 'Like unsuccessful.'
UNLIKE_UNSUCCESSFUL = 'Removing like unsuccessful.'
UNLIKE_SUCCESSFUL = 'Removing like successful.'
ALREADY_LIKED = 'Already liked.'
NOT_LIKED = 'Not already liked.'
INVALID_REQUEST = 'Invalid request.'


class Like(Resource):
    # For liking a story
    @jwt_required
    def post(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Create an object using request data
        like_object = like_schema.load(request.get_json())
        # Creating an for the requesting active user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Check target story is present and has valid status
        discovered_story = StoryModel.find_story_by_sid(like_object.target)
        if discovered_story is None or discovered_story.status == 'unapproved':
            return {'message': INVALID_REQUEST}, 500
        # Check if the requesting user is the author of target story or not
        if like_object.target in [story.sid for story in active_user_object.submissions]:
            return {'message': CANNOT_LIKE_OWN_STORY}, 400
        # Check if the requesting user has already liked the target story
        if like_object.target in [story.target for story in active_user_object.favourites]:
            return {'message': ALREADY_LIKED}, 400
        # If valid then fill the object fields with remaining data
        like_object.source = current_user
        like_object.time = time.asctime(time.localtime(time.time()))
        # Check for write errors and return appropriate messages
        if like_object.create_entry() == ERROR_WRITING_LIKE_TABLE:
            return {'message': LIKE_UNSUCCESSFUL}, 500
        # Now add the number of likes by one
        StoryModel.add_likes_by_one(like_object.target)
        # Send a success message
        return {'message': LIKE_SUCCESSFUL}, 202

    # For taking back like from a story
    @jwt_required
    def delete(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Create an object using request data
        unlike_object = like_schema.load(request.get_json())
        # Check target story is present and has valid status
        discovered_story = StoryModel.find_story_by_sid(unlike_object.target)
        if discovered_story is None or discovered_story.status == 'unapproved':
            return {'message': INVALID_REQUEST}, 500
        # Creating an for the requesting active user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Check if the requesting user is the author of target story or not
        if unlike_object.target in [story.sid for story in active_user_object.submissions]:
            return {'message': CANNOT_UNLIKE_OWN_STORY}, 400
        # Run a loop for checking and perform database operation
        for list_item in active_user_object.favourites:
            if list_item.target == unlike_object.target:
                if list_item.delete_entry() == ERROR_DELETING_LIKE_TABLE:
                    return {'message': UNLIKE_UNSUCCESSFUL}, 500
                else:
                    # Now reduce the number of likes by one
                    StoryModel.reduce_likes_by_one(unlike_object.target)
                    return {'message': UNLIKE_SUCCESSFUL}, 200
        return {'message': NOT_LIKED}, 400

