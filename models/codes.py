from db import db


ERROR_WRITING_CODES_TABLE = 'Error writing codes table.'


class CodeModel(db.Model):

    __tablename__ = 'codes'

    email = db.Column(db.VARCHAR(100), primary_key=True)
    code = db.Column(db.SMALLINT, nullable=False, unique=True)

    @classmethod
    def find_entry_by_code(cls, query_code):
        return cls.query.filter_by(code=query_code).first()

    def create_new_entry(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            return ERROR_WRITING_CODES_TABLE
