import time
from flask import request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from flask_restful import Resource

from schemas.follow import FollowSchema
from models.active import ActiveModel
from models.follow import (
    ERROR_WRITING_FOLLOW_TABLE,
    ERROR_DELETING_FOLLOW_TABLE
)

follow_schema = FollowSchema()

CANNOT_FOLLOW_ONESELF = 'You cannot follow yourself.'
CANNOT_UNFOLLOW_ONESELF = 'You cannot unfollow yourself.'
FOLLOW_SUCCESSFUL = 'Follow Successful.'
FOLLOW_UNSUCCESSFUL = 'Follow Unsuccessful.'
UNFOLLOW_UNSUCCESSFUL = 'Unfollow unsuccessful.'
UNFOLLOW_SUCCESSFUL = 'Unfollow Successful.'
ALREADY_FOLLOWING = 'Already Following.'
NOT_FOLLOWING = 'Not Following.'
INVALID_REQUEST = 'Invalid request.'


class Follow(Resource):
    # For following another user
    @jwt_required
    def post(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Create an object using request data
        follow_object = follow_schema.load(request.get_json())
        # Check if the requesting user is the same as the target
        if current_user == follow_object.target:
            return {'message': CANNOT_FOLLOW_ONESELF}
        # Find the target user for request validation
        active_user_object = ActiveModel.find_entry_by_uid(follow_object.target)
        if active_user_object is None:
            return {'message': INVALID_REQUEST}
        # Make an object of current user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Check if already following
        if follow_object.target in [user.target for user in active_user_object.following]:
            return {'message': ALREADY_FOLLOWING}
        # Add the additional data and write into database
        follow_object.source = current_user
        follow_object.time = time.asctime(time.localtime(time.time()))
        if follow_object.create_entry() == ERROR_WRITING_FOLLOW_TABLE:
            return {'message': FOLLOW_UNSUCCESSFUL}, 500
        return {'message': FOLLOW_SUCCESSFUL}, 202

    # For unfollowing another user
    @jwt_required
    def delete(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Create an object using request data
        unfollow_object = follow_schema.load(request.get_json())
        # Check if the requesting user is the same as the target
        if current_user == unfollow_object.target:
            return {'message': CANNOT_UNFOLLOW_ONESELF}
        # Find the target user for request validation
        active_user_object = ActiveModel.find_entry_by_uid(unfollow_object.target)
        if active_user_object is None:
            return {'message': INVALID_REQUEST}
        # Make an object of current user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Run a loop for checking and perform database operation
        for list_item in active_user_object.following:
            if list_item.target == unfollow_object.target:
                if list_item.delete_entry() == ERROR_DELETING_FOLLOW_TABLE:
                    return {'message': UNFOLLOW_UNSUCCESSFUL}, 500
                else:
                    return {'message': UNFOLLOW_SUCCESSFUL}, 200
        return {'message': NOT_FOLLOWING}, 400
