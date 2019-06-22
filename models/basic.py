from sqlalchemy.exc import SQLAlchemyError

from db import db

ERROR_WRITING_BASIC_TABLE = 'Error writing basic table.'


class BasicModel(db.Model):

    __tablename__ = 'basic'

    sno = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    uid = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'), nullable=False)
    dob = db.Column(db.DATE, nullable=False)
    bio = db.Column(db.VARCHAR(500), nullable=False)
    country = db.Column(db.VARCHAR(60), nullable=False)
    profession = db.Column(db.VARCHAR(20), nullable=False)
    image = db.Column(db.VARCHAR(50), nullable=False)

    def create_entry(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_BASIC_TABLE

