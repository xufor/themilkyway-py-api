import time
from flask import request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from flask_restful import Resource

from schemas.view import ViewSchema
from schemas.story import StorySchema
from models.active import ActiveModel
from models.stories import StoryModel
from models.views import (
    ERROR_WRITING_VIEWS_TABLE,
)

view_schema = ViewSchema()
story_schema = StorySchema()

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
            ActiveModel.add_views_by_one(discovered_story.author.uid)
        # Use dump to create a dictionary
        story_data = story_schema.dump(discovered_story)
        # Pop status and add the name of the author
        story_data.pop('status')
        story_data.pop('author')
        story_data.pop('viewers')
        story_data.pop('fans')
        story_data['name'] = discovered_story.author.name
        story_data['uid'] = discovered_story.author.uid
        return story_data



