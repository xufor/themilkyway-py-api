import time
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
CONFIRMATION_SUCCESSFUL = 'User successfully confirmed.'
SERVER_ERROR = 'Internal server error.'


class Confirm(Resource):
    @classmethod
    def get(cls, code):

        confirm_data = confirm_schema.load({'code': code})

        headers = {'Content-Type': 'text/html'}

        discovered_inactive_user = InactiveModel.find_entry_by_code(confirm_data['code'])
        if discovered_inactive_user is None:
            return make_response(render_template('conf_page.html', message=INVALID_LINK), 200, headers)
        else:
            indicator = discovered_inactive_user.delete_inactive_user()
            if indicator == ERROR_DELETING_INACTIVE_TABLE:
                return make_response(render_template('conf_page.html', message=SERVER_ERROR), 500, headers)

            # Dumping the fetched inactive object into a inactive data dictionary
            inactive_user_data = inactive_schema.dump(discovered_inactive_user)
            # Removing the code field from inactive data
            inactive_user_data.pop('code')
            # Creating an active schema object using available inactive data
            active_user_object = active_schema.load(inactive_user_data, db.session)
            # Adding the time field using the inbuilt time module
            active_user_object.time = time.asctime(time.localtime(time.time()))
            # Adding the uid field using inbuilt uuid module
            active_user_object.uid = ActiveModel.generate_fresh_uid()

            if active_user_object.create_active_user() == ERROR_WRITING_ACTIVE_TABLE:
                discovered_inactive_user.create_inactive_user()
                return make_response(render_template('conf_page.html', message=SERVER_ERROR), 500, headers)
            else:
                return make_response(render_template('conf_page.html', message=CONFIRMATION_SUCCESSFUL), 200, headers)


