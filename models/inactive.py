import os
import uuid
from sqlalchemy.exc import SQLAlchemyError
from sendgrid import SendGridAPIClient

from db import db

ERROR_WRITING_INACTIVE_TABLE = 'Error writing inactive table.'
ERROR_DELETING_INACTIVE_TABLE = 'Error deleting from inactive table.'


class InactiveModel(db.Model):
    __tablename__ = 'inactive'

    email = db.Column(db.VARCHAR(100), primary_key=True)
    time = db.Column(db.TIMESTAMP, nullable=False)
    name = db.Column(db.VARCHAR(80), nullable=False)
    password = db.Column(db.VARCHAR(60), nullable=False)
    code = db.Column(db.VARCHAR(64), nullable=False, unique=True)

    # Please use this convention of saying query_email or any other parameter instead of
    # only writing email.
    @classmethod
    def find_entry_by_email(cls, query_email):
        return cls.query.get(query_email)

    @classmethod
    def send_email(cls, inactive_user_object):
        verification_code = cls.generate_fresh_code()

        message = {
            'personalizations': [
                {
                    'to': [
                        {
                            'email': inactive_user_object.email
                        }
                    ],
                    'dynamic_template_data': {
                        'data': {
                            'link': f'https://www.themilkyway.ml/confirm/{verification_code}',
                            'name': inactive_user_object.name.split()[0]
                        }
                    }
                }
            ],
            'from': {
                'email': 'tmw.mission.control@gmail.com',
                'name': 'New Account Confirmation'
            },
            'template_id': 'd-7c633f38aec249e7817c026f3a20a321'
        }

        sg = SendGridAPIClient(os.getenv('EMAIL_API_KEY', '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'))
        response = sg.send(message)

        if response.status_code == 202:
            return {'code': verification_code}

    @classmethod
    def generate_random_code(cls):
        return uuid.uuid4().hex.lower() + uuid.uuid4().hex.lower()

    @classmethod
    def generate_fresh_code(cls):
        fresh_code = cls.generate_random_code()
        while cls.find_entry_by_code(fresh_code) is not None:
            fresh_code = cls.generate_random_code()
        return fresh_code

    @classmethod
    def find_entry_by_code(cls, query_code):
        return cls.query.filter_by(code=query_code).first()

    def create_inactive_user(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_INACTIVE_TABLE

    def delete_inactive_user(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_DELETING_INACTIVE_TABLE
