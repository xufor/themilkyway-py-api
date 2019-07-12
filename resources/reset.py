import datetime
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from schemas.reset import ResetSchema
from models.active import ActiveModel

reset_schema = ResetSchema()

OP_SUCCESSFUL = 'Operation successful.'


class Reset(Resource):
    @classmethod
    def post(cls):
        # Extract the email
        reset_data = reset_schema.load(request.get_json())
        # Now check if an active user exists
        discovered_active_user = ActiveModel.find_entry_by_email(reset_data['email'])
        if discovered_active_user is None:
            return {'message': 'No such account exists.'}, 400
        else:
            code = create_access_token(discovered_active_user.uid, False, datetime.timedelta(seconds=5))
            return {
                'message': OP_SUCCESSFUL,
                'link': f'http://localhost:3000/update/{code}'
            }
