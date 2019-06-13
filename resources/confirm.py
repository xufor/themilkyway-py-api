from db import db
from flask_restful import Resource
from flask import (
    make_response,
    render_template
)

from models.active import (
    ActiveModel,
    ERROR_WRITING_ACTIVE_TABLE
)
from models.inactive import (
    InactiveModel,
    ERROR_DELETING_INACTIVE_TABLE
)
from schemas.active import ActiveSchema
from schemas.inactive import InactiveSchema
from schemas.confirm import ConfirmSchema


active_schema = ActiveSchema()
inactive_schema = InactiveSchema()
confirm_schema = ConfirmSchema()

INVALID_LINK = 'The provided link is invalid.'
CONFIRMATION_FAILED = 'User confirmation failed.'
SERVER_ERROR = 'Internal server error occurred.'
CONFIRMATION_SUCCESSFUL = 'User successfully confirmed.'


class Confirm(Resource):
    @classmethod
    def get(cls, code):
        incoming_data = {'code': code}
        confirm_data = confirm_schema.load(incoming_data)

        headers = {'Content-Type': 'text/html'}

        discovered_inactive_user = InactiveModel.find_entry_by_code(confirm_data['code'])
        if discovered_inactive_user is None:
            return make_response(render_template('conf_page.html', message=INVALID_LINK), 200, headers)
        else:
            indicator = discovered_inactive_user.delete_inactive_user()
            if indicator == ERROR_DELETING_INACTIVE_TABLE:
                return make_response(render_template('conf_page.html', message=SERVER_ERROR), 500, headers)

            inactive_user_data = inactive_schema.dump(discovered_inactive_user)
            inactive_user_data['uid'] = ActiveModel.generate_fresh_uid()
            inactive_user_data.pop('code')
            active_user_object = active_schema.load(inactive_user_data, db.session)

            indicator = active_user_object.create_active_user()
            if indicator == ERROR_WRITING_ACTIVE_TABLE:
                discovered_inactive_user.create_inactive_user()
                return make_response(render_template('conf_page.html', message=SERVER_ERROR), 500, headers)
            else:
                return make_response(render_template('conf_page.html', message=CONFIRMATION_SUCCESSFUL), 200, headers)


