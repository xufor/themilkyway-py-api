import random
from db import db

ERROR_WRITING_CODES_TABLE = 'Error writing codes table.'
ERROR_DELETING_CODES_TABLE = 'Error deleting from codes table.'


class CodeModel(db.Model):

    __tablename__ = 'codes'

    email = db.Column(db.VARCHAR(100), primary_key=True)
    code = db.Column(db.SMALLINT, nullable=False, unique=True)

    @classmethod
    def find_entry_by_code(cls, query_code):
        return cls.query.filter_by(code=query_code).first()

    @classmethod
    def find_entry_by_email(cls, query_email):
        return cls.query.filter_by(email=query_email).first()

    @classmethod
    def generate_random_code(cls):
        return random.randint(999, 10000)

    @classmethod
    def generate_fresh_code(cls):
        fresh_code = cls.generate_random_code()
        while cls.find_entry_by_code(fresh_code) is not None:
            fresh_code = cls.generate_random_code()
            if cls.find_entry_by_code(fresh_code) is None:
                return fresh_code
        return fresh_code

    def create_code_entry(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            return ERROR_WRITING_CODES_TABLE

    def delete_code_entry(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return ERROR_DELETING_CODES_TABLE

