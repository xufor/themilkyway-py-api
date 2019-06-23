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
from models.basic import ERROR_WRITING_BASIC_TABLE
from resources.elite import NO_IMAGE_AVAILABLE


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
        if not(len(preference_list) == 3 and set(preference_list).issubset(set(genres))):
            return {'message': INVALID_PREFERENCES}
        # Creating an for the requesting active user
        active_user_object = ActiveModel.find_entry_by_uid(current_user)
        # Check if basic data already exists
        # If no image was uploaded the the frontend is expected to send the field empty.
        existing_basic_object = active_user_object.basic
        if not existing_basic_object:
            fresh_basic_object.uid = current_user
            if fresh_basic_object.create_entry() == ERROR_WRITING_BASIC_TABLE:
                return {'message': UPDATE_UNSUCCESSFUL}
            return {'message': UPDATE_SUCCESSFUL}
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
                    'basic': basic_schema.dump(active_user_object.basic) if
                    not active_user_object.basic or not active_user_object.basic.private
                    else IS_PRIVATE,
                    'stories': [{
                        'sid': story.sid,
                        'uid': story.uid,
                        'title': story.title,
                        'name': story.author.name,
                        'summary': story.summary
                    } for story in active_user_object.submissions],
                    'following': [{
                        'uid': following.target,
                        'name': following.following.name
                    } for following in active_user_object.following]
                    if (not active_user_object.basic.private) else IS_PRIVATE,
                    'followers': [{
                        'uid': followers.source,
                        'name': followers.followers.name,
                        'image': followers.followers.basic.image
                        if (followers.followers.basic and followers.followers.basic.image)
                        else NO_IMAGE_AVAILABLE
                    } for followers in active_user_object.followers],
                    'favourites': [{
                        'uid': like.liked.uid,
                        'sid': like.liked.sid,
                        'name': like.liked.author.name,
                        'summary': like.liked.summary,
                        'title': like.liked.title
                    } for like in active_user_object.favourites]
                    if (not active_user_object.basic.private) else IS_PRIVATE,
                    'achievements': {
                        'views': active_user_object.views,
                        'likes': active_user_object.likes
                    }
                }
        else:
            # Create an object using request data
            active_user_object = ActiveModel.find_entry_by_uid(get_jwt_identity())
            return {
                 'basic': basic_schema.dump(active_user_object.basic),
                 'stories': [{
                     'sid': story.sid,
                     'uid': story.uid,
                     'title': story.title,
                     'name': story.author.name,
                     'summary': story.summary
                 } for story in active_user_object.submissions],
                 'following': [{
                     'uid': following.target,
                     'name': following.following.name
                 } for following in active_user_object.following],
                 'followers': [{
                     'uid': followers.source,
                     'name': followers.followers.name,
                     'image': followers.followers.basic.image
                     if (followers.followers.basic and followers.followers.basic.image)
                     else NO_IMAGE_AVAILABLE
                 } for followers in active_user_object.followers],
                 'favourites': [{
                     'uid': like.liked.uid,
                     'sid': like.liked.sid,
                     'name': like.liked.author.name,
                     'summary': like.liked.summary,
                     'title': like.liked.title
                 } for like in active_user_object.favourites],
                 'achievements': {
                     'views': active_user_object.views,
                     'likes': active_user_object.likes
                 }
             }





