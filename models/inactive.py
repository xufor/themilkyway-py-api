from db import db
from sqlalchemy.exc import SQLAlchemyError

from models.codes import CodeModel

ERROR_WRITING_INACTIVE_TABLE = 'Error writing inactive table.'
ERROR_DELETING_INACTIVE_TABLE = 'Error deleting from inactive table.'


class InactiveModel(db.Model):
    __tablename__ = 'inactive'

    email = db.Column(db.VARCHAR(100), primary_key=True)
    name = db.Column(db.VARCHAR(80), nullable=False)
    password = db.Column(db.VARCHAR(60), nullable=False)

    # Please use this convention of saying query_email or any other parameter instead of
    # only writing email.
    @classmethod
    def find_entry_by_email(cls, query_email):
        return cls.query.filter_by(email=query_email).first()

    @classmethod
    def send_email(cls, recipient):
        verification_code = CodeModel.generate_fresh_code()
        response_code = 200
        if response_code == 200:
            return {'email': recipient, 'code': verification_code}

    def create_inactive_user(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            return ERROR_WRITING_INACTIVE_TABLE

    def delete_inactive_user(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError:
            return ERROR_DELETING_INACTIVE_TABLE
