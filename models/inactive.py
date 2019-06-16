import uuid
from sqlalchemy.exc import SQLAlchemyError

from db import db

ERROR_WRITING_INACTIVE_TABLE = 'Error writing inactive table.'
ERROR_DELETING_INACTIVE_TABLE = 'Error deleting from inactive table.'


class InactiveModel(db.Model):
    __tablename__ = 'inactive'

    email = db.Column(db.VARCHAR(100), primary_key=True)
    time = db.Column(db.TIMESTAMP, nullable=False)
    name = db.Column(db.VARCHAR(80), nullable=False)
    password = db.Column(db.VARCHAR(60), nullable=False)
    code = db.Column(db.VARCHAR(32), nullable=False, unique=True)

    # Please use this convention of saying query_email or any other parameter instead of
    # only writing email.
    @classmethod
    def find_entry_by_email(cls, query_email):
        return cls.query.filter_by(email=query_email).first()

    @classmethod
    def send_email(cls, recipient):
        verification_code = cls.generate_fresh_code()
        response_code = 200
        if response_code == 200:
            return {'email': recipient, 'code': verification_code}

    @classmethod
    def generate_random_code(cls):
        return uuid.uuid4().hex.lower()

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
