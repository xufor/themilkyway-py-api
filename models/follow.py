from db import db
from sqlalchemy.exc import SQLAlchemyError

ERROR_WRITING_FOLLOW_TABLE = 'Error writing follow table.'
ERROR_DELETING_FOLLOW_TABLE = 'Error deleting from follow table.'


class FollowModel(db.Model):

    __tablename__ = 'follow'

    sno = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    initiator = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'))
    target = db.Column(db.VARCHAR(6), nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)

    def create_entry(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_FOLLOW_TABLE

    def delete_entry(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_DELETING_FOLLOW_TABLE


