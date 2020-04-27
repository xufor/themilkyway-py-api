import os
import datetime
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from sendgrid import SendGridAPIClient

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
            code = create_access_token(discovered_active_user.uid, False, datetime.timedelta(minutes=5))

            message = {
                'personalizations': [
                    {
                        'to': [
                            {
                                'email': discovered_active_user.email
                            }
                        ],
                        'dynamic_template_data': {
                            'data': {
                                'link': f'https://www.themilkyway.tk/update/{code}',
                                'name': discovered_active_user.name.split()[0]
                            }
                        }
                    }
                ],
                'from': {
                    'email': 'admin@tmw.com',
                    'name': 'Password Reset'
                },
                'template_id': 'Here goes the template id!'
            }

            sg = SendGridAPIClient(os.getenv('EMAIL_API_KEY', 'Here goes the default API Key!'))
            response = sg.send(message)

            if response.status_code == 202:
                return {'message': OP_SUCCESSFUL}
