import bcrypt
from flask import request
from flask_restful import Resource
from flask_jwt_extended import decode_token

from models.active import ActiveModel, ERROR_WRITING_ACTIVE_TABLE
from schemas.update import UpdateSchema
from resources.signup import INVALID_PASSWORD_LENGTH

update_schema = UpdateSchema()

PASSWORD_SUCCESSFULLY_UPDATED = 'Password successfully updated.'
PASSWORD_COULD_NOT_BE_UPDATED = 'Password updation failed.'


class Change(Resource):
    @classmethod
    def post(cls):
        # Extract the required data
        update_data = update_schema.load(request.get_json())
        # Get the identity
        target_uid = decode_token(update_data['token'])['identity']
        # Find active user
        active_user_object = ActiveModel.find_entry_by_uid(target_uid)
        # Update the password
        encoded_password = update_data['password'].encode()
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        active_user_object.password = hashed_password.decode()
        # Write the changes
        if active_user_object.create_active_user() == ERROR_WRITING_ACTIVE_TABLE:
            return {'message': PASSWORD_COULD_NOT_BE_UPDATED}, 500
        # Return success
        return {'message': PASSWORD_SUCCESSFULLY_UPDATED}



