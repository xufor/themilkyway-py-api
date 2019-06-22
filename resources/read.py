import time
from flask import request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from flask_restful import Resource

from schemas.view import ViewSchema
from models.active import ActiveModel
from models.stories import StoryModel
from models.views import (
    ERROR_WRITING_VIEWS_TABLE,
)

view_schema = ViewSchema()

VIEW_SUCCESSFUL = 'View Successful.'
VIEW_UNSUCCESSFUL = 'View Unsuccessful.'
INVALID_REQUEST = 'Invalid request.'


class Read(Resource):
    # For following another user
    @jwt_required
    def post(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Create an object using request data
        view_object = view_schema.load(request.get_json())
        # Check if the target valid or not
        discovered_story = StoryModel.find_story_by_sid(view_object.target)
        if discovered_story is None or discovered_story.status == 'unapproved':
            return {'message': INVALID_REQUEST}
        # Make an object of current user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Check if already viewed or not
        if view_object.target not in [view.target for view in active_user_object.viewed]:
            view_object.source = current_user
            view_object.time = time.asctime(time.localtime(time.time()))
            if view_object.create_entry() == ERROR_WRITING_VIEWS_TABLE:
                return {'message': VIEW_UNSUCCESSFUL}, 500
            # Add the number of views by one
            StoryModel.add_views_by_one(view_object.target)
        # Return the requested story
        return {
            'uid': discovered_story.uid,
            'sid': discovered_story.sid,
            'story': discovered_story.story,
            'title': discovered_story.title,
            'summary': discovered_story.summary,
            'likes': discovered_story.likes,
            'name': discovered_story.author.name,
            'views': discovered_story.views,
            'time': str(discovered_story.time),
        }



