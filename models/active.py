import uuid
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.stories import StoryModel  # Do not remove
from models.follow import FollowModel  # Do not remove
from models.like import LikeModel      # Do not remove


ERROR_WRITING_ACTIVE_TABLE = 'Error writing active table.'


class ActiveModel(db.Model):

    __tablename__ = 'active'

    uid = db.Column(db.VARCHAR(6), primary_key=True)
    time = db.Column(db.TIMESTAMP, nullable=False)
    name = db.Column(db.VARCHAR(80), nullable=False)
    email = db.Column(db.VARCHAR(100), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(60), nullable=False)
    submissions = db.relationship('StoryModel', backref='author', lazy='dynamic')
    following = db.relationship('FollowModel', foreign_keys='FollowModel.source',
                                backref='followers', lazy='dynamic')
    followers = db.relationship('FollowModel', foreign_keys='FollowModel.target',
                                backref='following', lazy='dynamic')
    favourites = db.relationship('LikeModel', foreign_keys='LikeModel.source',
                                 backref='fan', lazy='dynamic')

    @classmethod
    def find_entry_by_email(cls, query_email):
        return cls.query.filter_by(email=query_email).first()

    @classmethod
    def find_entry_by_uid(cls, query_uid):
        return cls.query.filter_by(uid=query_uid).first()

    @classmethod
    def generate_random_uid(cls):
        return uuid.uuid4().hex.lower()[0:6]

    @classmethod
    def generate_fresh_uid(cls):
        fresh_uid = cls.generate_random_uid()
        while cls.find_entry_by_uid(fresh_uid) is not None:
            fresh_uid = cls.generate_random_code()
        return fresh_uid

    def create_active_user(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_ACTIVE_TABLE

    def delete_active_user(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
