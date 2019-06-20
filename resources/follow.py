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
NOT_FOLLOWING = 'Not Following'


class Follow(Resource):
    # For following another user
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        follow_object = follow_schema.load(request.get_json())
        if current_user == follow_object.target:
            return {'message': CANNOT_FOLLOW_ONESELF}
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        for listItem in active_user_object.following:
            if listItem.target == follow_object.target:
                return {'message': ALREADY_FOLLOWING}
        else:
            follow_object.initiator = get_jwt_identity()
            follow_object.time = time.asctime(time.localtime(time.time()))
            if follow_object.create_entry() == ERROR_WRITING_FOLLOW_TABLE:
                return {'message': FOLLOW_UNSUCCESSFUL}, 500
        return {'message': FOLLOW_SUCCESSFUL}, 202

    # For unfollowing another user
    @jwt_required
    def delete(self):
        current_user = get_jwt_identity()
        unfollow_object = follow_schema.load(request.get_json())
        if current_user == unfollow_object.target:
            return {'message': CANNOT_UNFOLLOW_ONESELF}
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        for listItem in active_user_object.following:
            if listItem.target == unfollow_object.target:
                if listItem.delete_entry() == ERROR_DELETING_FOLLOW_TABLE:
                    return {'message': UNFOLLOW_UNSUCCESSFUL}, 500
                return {'message': UNFOLLOW_SUCCESSFUL}, 200
            return {'message': NOT_FOLLOWING}, 400
