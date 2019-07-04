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

NO_MORE_FEED = 'Cannot generate more feed.'


# An algorithm that filters duplicates and self composed stories
def return_unique_list(object_list, active_uid):
    filtered_list = []
    for story in object_list:
        if story.uid not in [uid for uid in filtered_list] and story.uid != active_uid:
            filtered_list.append(story)
    return filtered_list


class Feed(Resource):
    @jwt_required
    def post(self):
        # Parse incoming data and extract required field
        feed_data = feed_schema.load(request.get_json())
        incoming_version = feed_data['version']
        # Create an object of the active user
        active_user_object = ActiveModel.find_entry_by_uid(get_jwt_identity())
        # The final list to be returned
        genre_based_list, follow_based_list, final_list = [], [], []
        if active_user_object.basic is not None:
            preferences_list = active_user_object.basic.preferences.split(',')
            # append fetched stories for every preference
            for preference in preferences_list:
                genre_based_list.append(StoryModel.find_feed_stories_by_genre(preference, incoming_version))
        # Set counter to zero
        ctr = 0
        for user in active_user_object.following:
            # This will set a limit at the maximum no. of stories that can be selected
            if ctr > incoming_version*5:
                break
            latest_user_story = StoryModel.find_latest_story_by_uid(user.target)
            if latest_user_story is not None:
                follow_based_list.append(latest_user_story)
                ctr += 1
        # Slice all the elementary lists
        for sub_list in genre_based_list:
            sub_list = sub_list[(incoming_version-1)*5:]
            final_list.extend(sub_list)
        final_list.extend(follow_based_list[(incoming_version-1)*5:])
        # Now filter the list for duplicated and self composed stories
        final_list = return_unique_list(final_list, active_user_object.uid)
        # Return the results or send an error if final list is empty
        if len(final_list) != 0:
            return {'results': [StoryModel.generate_feed_element_data(story) for story in final_list]}
        else:
            return {'message': NO_MORE_FEED}, 400
