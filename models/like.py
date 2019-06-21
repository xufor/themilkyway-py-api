from db import db
from sqlalchemy.exc import SQLAlchemyError

ERROR_WRITING_LIKE_TABLE = 'Error writing likes table.'
ERROR_DELETING_LIKE_TABLE = 'Error deleting from likes table.'


class LikeModel(db.Model):

    __tablename__ = 'like'

    sno = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    source = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'), nullable=False)
    target = db.Column(db.VARCHAR(8), db.ForeignKey('stories.sid'), nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)

    def create_entry(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_LIKE_TABLE

    def delete_entry(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_DELETING_LIKE_TABLE


