import requests
from db import db


API_KEY = '1b224ebb78617da4e9ad19be9e63c827-87cdd773-8b475528'
DOMAIN_NAME = 'sandboxb76eaae72b344ac39b9e5bd1f0768fb5.mailgun.org'


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
            data={'from': f'TheMilkyWay <postmaster@{DOMAIN_NAME}>',
                  'to': ['New User', f'<{recipient}>'],
                  'subject': 'Your registration code is here!',
                  'text': f'Your registration code for email id {recipient} is {code}'
                  }
        )
