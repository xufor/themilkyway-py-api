import uuid
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.like import LikeModel  # Do not delete

ERROR_WRITING_STORY_TABLE = 'Error writing story table.'
ERROR_DELETING_STORY_TABLE = 'Error deleting from story table.'


class StoryModel(db.Model):

    __tablename__ = 'stories'

    sid = db.Column(db.VARCHAR(8), primary_key=True)
    uid = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'))
    status = db.Column(db.VARCHAR(10), nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)
    title = db.Column(db.VARCHAR(500), nullable=False)
    summary = db.Column(db.TEXT, nullable=False)
    story = db.Column(db.TEXT, nullable=False)
    reads = db.Column(db.BIGINT, nullable=False)
    likes = db.Column(db.BIGINT, nullable=False)
    fans = db.relationship('LikeModel', foreign_keys='LikeModel.target',
                           backref='favourite', lazy='dynamic')

    @classmethod
    def find_entry_by_sid(cls, query_sid):
        return cls.query.filter_by(sid=query_sid).first()

    @classmethod
    def find_entry_by_uid(cls, query_uid):
        return cls.query.filter_by(uid=query_uid).first()

    @classmethod
    def generate_random_sid(cls):
        return uuid.uuid4().hex.lower()[0:8]

    @classmethod
    def generate_fresh_sid(cls):
        fresh_sid = cls.generate_random_sid()
        while cls.find_entry_by_sid(fresh_sid) is not None:
            fresh_sid = cls.generate_random_sid()
        return fresh_sid

    @classmethod
    def find_story_by_sid(cls, query_sid):
        return cls.query.filter_by(sid=query_sid).first()

    def create_story(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_STORY_TABLE

    def delete_story(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_DELETING_STORY_TABLE
