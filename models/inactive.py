import random
from db import db

from models.codes import CodeModel

ERROR_WRITING_INACTIVE_TABLE = 'Error writing inactive table.'


class InactiveModel(db.Model):
    __tablename__ = 'inactive'

    name = db.Column(db.VARCHAR(80), nullable=False, primary_key=True)
    email = db.Column(db.VARCHAR(100), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(100), nullable=False, unique=True)

    # Please use this convention of saying query_email or any other parameter instead of
    # only writing email.
    @classmethod
    def find_entry_by_email(cls, query_email):
        return cls.query.filter_by(email=query_email).first()

    @classmethod
    def send_email(cls, recipient):
        verification_code = cls.generate_fresh_code()
        print(verification_code)
        response_code = 200
        if response_code == 200:
            return {'email': recipient, 'code': verification_code}

    @classmethod
    def generate_random_code(cls):
        return random.randint(999, 10000)

    @classmethod
    def generate_fresh_code(cls):
        fresh_code = cls.generate_random_code()
        while CodeModel.find_entry_by_code(fresh_code) is not None:
            fresh_code = cls.generate_random_code()
            if CodeModel.find_entry_by_code(fresh_code) is None:
                return fresh_code
        return fresh_code

    def create_inactive_user(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            return ERROR_WRITING_INACTIVE_TABLE


