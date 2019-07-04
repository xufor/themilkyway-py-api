import time
import datetime
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from db import db
from schemas.story import StorySchema
from schemas.edit import EditSchema
from schemas.approve import ApproveSchema
from resources.profile import genres
from models.active import (
    ActiveModel,
    ERROR_WRITING_ACTIVE_TABLE
)
from models.stories import (
    StoryModel,
    ERROR_WRITING_STORY_TABLE,
    ERROR_DELETING_STORY_TABLE
)
from models.views import ERROR_DELETING_VIEWS_TABLE
from models.likes import ERROR_DELETING_LIKE_TABLE

story_schema = StorySchema()
edit_schema = EditSchema()
delete_schema = ApproveSchema()

ERROR_SUBMITTING_STORY = 'Error in submitting story.'
STORY_SUCCESSFULLY_SUBMITTED = 'Story successfully submitted.'
STORY_SUCCESSFULLY_UPDATED = 'Story successfully updated.'
INVALID_GENRE = 'The provided genres are not valid.'
INVALID_REQUEST = 'Invalid request.'
SUMMARY_TOO_LONG = 'Summary of and below 80 words is allowed.'
STORY_TOO_LONG = 'Story of and below 10000 words is allowed.'
TITLE_TOO_LONG = 'Title of and below 7 words is allowed.'
OPERATION_UNSUCCESSFUL = 'Operation unsuccessful.'
OPERATION_SUCCESSFUL = 'Operation successful.'
NOT_BEFORE_A_DAY = 'Cannot submit next story before 24 hours.'


class Submit(Resource):
    # For submitting a story
    @jwt_required
    def post(self):
        # Get the latest story
        latest_story_object = StoryModel.force_find_latest_story_by_uid(get_jwt_identity())
        current_time = time.time()
        epoch = datetime.datetime.utcfromtimestamp(0)
        story_time = (latest_story_object.time - epoch).total_seconds()
        if (current_time-story_time) < 86400:
            return {'message': NOT_BEFORE_A_DAY}, 400
        # Loaded incoming data into story
        story_object = story_schema.load(request.get_json(), db.session)
        # Check if the the genres is valid or not
        # Accepts 3 genres only
        genre_list = story_object.genre.split(',')
        if not (len(genre_list) <= 3 and set(genre_list).issubset(set(genres))):
            return {'message': INVALID_GENRE}, 400
        # Check word length of various elements
        if StoryModel.words_counter(story_object.title) > 7:
            return {'message': TITLE_TOO_LONG}, 400
        if StoryModel.words_counter(story_object.summary) > 10:
            return {'message': SUMMARY_TOO_LONG}, 400
        if StoryModel.words_counter(story_object.story) > 5:
            return {'message': STORY_TOO_LONG}, 400
        # Adding time, uid and sid fields to story object
        story_object.time = time.asctime(time.gmtime(time.time()))
        story_object.uid = get_jwt_identity()
        story_object.sid = StoryModel.generate_fresh_sid()
        story_object.status = 'unapproved'
        story_object.views = 0
        story_object.likes = 0
        # Creating a new entry in story table and checking for success
        if story_object.create_story() == ERROR_WRITING_STORY_TABLE:
            return {'message': ERROR_SUBMITTING_STORY}, 500
        return {'message': STORY_SUCCESSFULLY_SUBMITTED}, 201

    # For editing a story
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
            # Check the genre data
            genre_list = story_data['genre'].split(',')
            if not (len(genre_list) <= 3 and set(genre_list).issubset(set(genres))):
                return {'message': INVALID_GENRE}, 400
            # Check word length of various elements
            if StoryModel.words_counter(story_data['title']) > 7:
                return {'message': TITLE_TOO_LONG}, 400
            if StoryModel.words_counter(story_data['summary']) > 80:
                return {'message': SUMMARY_TOO_LONG}, 400
            if StoryModel.words_counter(story_data['story']) > 10000:
                return {'message': STORY_TOO_LONG}, 400
            # Now update the fields of the story
            discovered_story.story = story_data['story']
            discovered_story.summary = story_data['summary']
            discovered_story.title = story_data['title']
            discovered_story.genre = story_data['genre']
            if discovered_story.create_story() == ERROR_WRITING_STORY_TABLE:
                return {'message': ERROR_SUBMITTING_STORY}, 500
        return {'message': STORY_SUCCESSFULLY_UPDATED}, 200

    # For deleting a story
    @jwt_required
    def delete(self):
        # Extract and parse the data from request
        delete_data = delete_schema.load(request.get_json())
        # Create an object of requesting user
        active_user_object = ActiveModel.find_entry_by_uid(get_jwt_identity())
        # Check if the story is present in submissions and has valid status
        for story in active_user_object.submissions:
            if story.sid == delete_data['sid'] and StoryModel.check_story_status(story):
                # Set counter to zero
                ctr = 0
                # Delete all likes
                for fan in story.fans:
                    ctr += 1
                    if fan.delete_entry() == ERROR_DELETING_LIKE_TABLE:
                        return {'message': OPERATION_UNSUCCESSFUL}
                # Decrease the total likes of the user
                active_user_object.likes -= ctr
                # Set counter to zero
                ctr = 0
                # Delete all views
                for viewer in story.viewers:
                    ctr += 1
                    if viewer.delete_entry() == ERROR_DELETING_VIEWS_TABLE:
                        return {'message': OPERATION_UNSUCCESSFUL}
                # Decrease the total views of the user
                active_user_object.views -= ctr
                # Commit changes done to active user
                if active_user_object.create_active_user() == ERROR_WRITING_ACTIVE_TABLE:
                    return {'message': OPERATION_UNSUCCESSFUL}
                # Delete the story
                if story.delete_story() == ERROR_DELETING_STORY_TABLE:
                    return {'message': OPERATION_UNSUCCESSFUL}
                return {'message': OPERATION_SUCCESSFUL}
        return {'message': INVALID_REQUEST}
















