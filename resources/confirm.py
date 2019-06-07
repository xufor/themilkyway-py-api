from db import db
from flask_restful import Resource
from flask import request

from schemas.codes import CodeSchema
from models.codes import CodeModel
from models.active import (
    ActiveModel,
    ERROR_WRITING_ACTIVE_TABLE
)
from models.inactive import InactiveModel
from models.active import ActiveModel
from schemas.active import ActiveSchema
from schemas.inactive import InactiveSchema


code_schema = CodeSchema()
active_schema = ActiveSchema()
inactive_schema = InactiveSchema()

SIGN_UP_FIRST = 'Please sign up first.'
USER_ALREADY_REGISTERED = 'The user is already registered.'
INVALID_VERIFICATION_CODE = 'The provided code is invalid.'
CONFIRMATION_FAILED = 'User confirmation failed.'
CONFIRMATION_SUCCESSFUL = 'User successfully confirmed.'


class Confirm(Resource):
    @classmethod
    def post(cls):
        incoming_data = request.get_json()
        incoming_email = incoming_data['email']
        incoming_code = incoming_data['code']
        if InactiveModel.find_entry_by_email(incoming_email) is None:
            return {'message': SIGN_UP_FIRST}

        if ActiveModel.find_entry_by_email(incoming_email) is not None:
            return {'message': USER_ALREADY_REGISTERED}

        discovered_code_entry = CodeModel.find_entry_by_email(incoming_email)

        if discovered_code_entry is not None:
            if discovered_code_entry.code != incoming_code:
                return {'message': INVALID_VERIFICATION_CODE}
            else:
                discovered_inactive_user = InactiveModel.find_entry_by_email(incoming_email)
                discovered_inactive_user.delete_inactive_user()
                discovered_code_entry.delete_code_entry()
                inactive_user_data = inactive_schema.dump(discovered_inactive_user)
                inactive_user_data['uid'] = ActiveModel.generate_fresh_uid()
                active_user_object = active_schema.load(inactive_user_data, db.session)
                write_success_indicator = active_user_object.create_active_user()
                if write_success_indicator == ERROR_WRITING_ACTIVE_TABLE:
                    return {'message': CONFIRMATION_FAILED}, 500
                else:
                    return {'message': CONFIRMATION_SUCCESSFUL}, 200


