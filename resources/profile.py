from flask import request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
    jwt_optional
)
from flask_restful import Resource

from schemas.basic import BasicSchema
from schemas.profile import ProfileSchema
from models.active import ActiveModel
from models.stories import StoryModel
from models.basic import (
    BasicModel,
    ERROR_WRITING_BASIC_TABLE
)
from models.follow import FollowModel
from models.likes import LikesModel


basic_schema = BasicSchema()
profile_schema = ProfileSchema()

UPDATE_SUCCESSFUL = 'Update successful.'
UPDATE_UNSUCCESSFUL = 'Update unsuccessful.'
IS_PRIVATE = 'The author has decided not to show his private details.'
INVALID_REQUEST = 'Invalid request.'
INVALID_PREFERENCES = 'Invalid Preferences.'

genres = ['Classic', 'Crime', 'Fable', 'Fairy-Tale', 'Fan-Fiction', 'Fantasy', 'Folktale', 'Historical-Fiction',
          'Horror',  'Humor', 'Legend', 'Magic', 'Meta-Fiction', 'Mystery', 'Mythology', 'Mythopoeia',
          'Realistic-Fiction', 'Science-Fiction', 'Swashbuckler', 'Tall Tale', 'Memoir', 'Narrative', 'Adventure',
          'Erotic']


class Profile(Resource):
    # For updating profile
    @jwt_required
    def put(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Create an object using request data
        fresh_basic_object = basic_schema.load(request.get_json())
        # Validate the preferences
        preference_list = fresh_basic_object.preferences.split(',')
        if not(len(preference_list) <= 3 and set(preference_list).issubset(set(genres))):
            return {'message': INVALID_PREFERENCES}
        # Creating an for the requesting active user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Check if basic data already exists
        existing_basic_object = active_user_object.basic
        if existing_basic_object is None:
            fresh_basic_object.uid = current_user
            if fresh_basic_object.create_entry() == ERROR_WRITING_BASIC_TABLE:
                return {'message': UPDATE_UNSUCCESSFUL}, 500
            return {'message': UPDATE_SUCCESSFUL}, 201
        else: 
            # Update all fields with new data
            existing_basic_object.bio = fresh_basic_object.bio
            existing_basic_object.dob = fresh_basic_object.dob
            existing_basic_object.country = fresh_basic_object.country
            existing_basic_object.profession = fresh_basic_object.profession
            existing_basic_object.image = fresh_basic_object.image
            existing_basic_object.preferences = fresh_basic_object.preferences
            existing_basic_object.private = fresh_basic_object.private
            if existing_basic_object.create_entry() == ERROR_WRITING_BASIC_TABLE:
                return {'message': UPDATE_UNSUCCESSFUL}
            return {'message': UPDATE_SUCCESSFUL}

    # For fetching profile
    @jwt_optional
    def post(self):
        # Extract user who tends to like from jwt
        current_user = get_jwt_identity()
        # Check if the jwt was sent or not
        if not current_user:
            # Create an object using request data
            profile_object = profile_schema.load(request.get_json())
            active_user_object = ActiveModel.find_entry_by_uid(profile_object['uid'])
            if active_user_object is None:
                return {'message': INVALID_REQUEST}
            else:
                return {
                    # If basic data is not yet added then empty dict will be returned
                    # If data is kept private then appropriate message is returned
                    'basic': BasicModel.generate_basic_profile_data(active_user_object),
                    'stories': [StoryModel.generate_story_element_data(story) for story
                                in StoryModel.filter_story_object_list(active_user_object.submissions)],
                    'following': FollowModel.generate_following_profile_data(active_user_object),
                    'followers': FollowModel.generate_followers_profile_data(active_user_object),
                    'favourites': LikesModel.generate_favourites_profile_data(active_user_object),
                    'achievements': {
                        'views': active_user_object.views,
                        'likes': active_user_object.likes
                    }
                }
        else:
            # Create an object using request data
            active_user_object = ActiveModel.find_entry_by_uid(get_jwt_identity())
            return {
                 'basic': BasicModel.force_generate_basic_profile_data(active_user_object),
                 'stories': [StoryModel.generate_story_element_data(story) for story
                             in StoryModel.filter_story_object_list(active_user_object.submissions)],
                 'following': FollowModel.force_generate_following_profile_data(active_user_object),
                 'followers': FollowModel.generate_followers_profile_data(active_user_object),
                 'favourites': LikesModel.force_generate_favourites_profile_data(active_user_object),
                 'achievements': {
                     'views': active_user_object.views,
                     'likes': active_user_object.likes
                 }
             }





