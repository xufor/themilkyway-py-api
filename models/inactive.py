import requests
from db import db


API_KEY = '481dbd2e464fdd8a32f06f4ba0384658-87cdd773-b2959084'
DOMAIN_NAME = 'sandbox26adf25e50cb4cb187a89d14eb3f1fa9.mailgun.org'


class InactiveModel(db.Model):
    __tablename__ = 'inactive'

    name = db.Column(db.String(80), nullable=False, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=True)

    @classmethod
    def find_entry_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def send_email(cls, recipient, code):
        return requests.post(
            f'https://api.mailgun.net/v3/{DOMAIN_NAME}/messages',
            auth=('api', API_KEY),
            data={'from': f'Ayush Garg <mailgun@{DOMAIN_NAME}>',
                  'to': [recipient, DOMAIN_NAME],
                  'subject': 'Your registration code is here!',
                  'text': f'Your registration code for email id {recipient} is {code}'
                  }
        )
