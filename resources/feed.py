from flask import request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from flask_restful import Resource

from models.active import ActiveModel
from schemas.feed import FeedSchema
from models.stories import StoryModel

feed_schema = FeedSchema()


class Feed(Resource):
    @jwt_required
    def post(self):
        # Parse incoming data and extract required field
        feed_data = feed_schema.load(request.get_json())
        incoming_version = feed_data['version']
        # Create an object of the active user
        active_user_object = ActiveModel.find_entry_by_uid(get_jwt_identity())
        # The final list to be returned
        final_list = []
        if active_user_object.basic is not None:
            preferences_list = active_user_object.basic.preferences.split(',')
            for preference in preferences_list:
                final_list.extend(StoryModel.find_feed_stories_by_genre(preference, incoming_version))
        # Set counter to zero
        ctr = 0
        for user in active_user_object.following:
            # This will set a limit at the maximum no. of stories that can be selected
            if ctr > incoming_version*5:
                break
            latest_user_story = StoryModel.find_latest_story_by_uid(user.target)
            if (latest_user_story is not None) and (latest_user_story.sid not in [story.sid for story in final_list]):
                final_list.append(latest_user_story)
                ctr += 1

        return {'results': [StoryModel.generate_feed_element_data(story) for story in final_list]}
