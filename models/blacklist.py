from sqlalchemy.exc import SQLAlchemyError

from db import db

ERROR_WRITING_BLACKLIST_TABLE = 'Error writing blacklist table.'


class BlacklistModel(db.Model):

    __tablename__ = 'blacklist'

    jti = db.Column(db.VARCHAR(36), primary_key=True)
    time = db.Column(db.TIMESTAMP, nullable=False)

    @classmethod
    def check_jti_in_blacklist(cls, query_jti):
        if cls.query.filter_by(jti=query_jti).first() is not None:
            return True
        else:
            return False

    def blacklist_token(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_BLACKLIST_TABLE
