import uuid
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_

from db import db
from dummy import UID
from models.stories import StoryModel  # Do not remove
from models.follow import FollowModel  # Do not remove
from models.likes import LikesModel      # Do not remove
from models.views import ViewsModel    # Do not remove
from models.basic import BasicModel    # Do not remove


ERROR_WRITING_ACTIVE_TABLE = 'Error writing active table.'
NO_IMAGE_AVAILABLE = 'No Image available.'


class ActiveModel(db.Model):

    __tablename__ = 'active'

    uid = db.Column(db.VARCHAR(6), primary_key=True)
    time = db.Column(db.TIMESTAMP, nullable=False)
    name = db.Column(db.VARCHAR(80), nullable=False)
    email = db.Column(db.VARCHAR(100), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(60), nullable=False)
    views = db.Column(db.BIGINT, nullable=False)
    likes = db.Column(db.BIGINT, nullable=False)
    submissions = db.relationship('StoryModel', backref='author', lazy='dynamic')
    basic = db.relationship('BasicModel', backref='strong', uselist=False)
    following = db.relationship('FollowModel', foreign_keys='FollowModel.source',
                                backref='followers', lazy='dynamic')
    followers = db.relationship('FollowModel', foreign_keys='FollowModel.target',
                                backref='following', lazy='dynamic')
    favourites = db.relationship('LikesModel', foreign_keys='LikesModel.source',
                                 backref='fan', lazy='dynamic')
    viewed = db.relationship('ViewsModel', foreign_keys='ViewsModel.source',
                             backref='viewers', lazy='dynamic')

    @classmethod
    def find_entry_by_email(cls, query_email):
        return cls.query.filter_by(email=query_email).first()

    @classmethod
    def find_entry_by_name(cls, query_name, version, current_user):
        return cls.query.filter(and_(cls.name.ilike(f'%{query_name}%'), cls.uid != current_user)).limit(version*15).all()

    @classmethod
    def find_entry_by_uid(cls, query_uid):
        return cls.query.get(query_uid)

    @classmethod
    def generate_random_uid(cls):
        return uuid.uuid4().hex.lower()[0:6]

    @classmethod
    def generate_elite_users(cls):
        return cls.query.filter(cls.uid != UID[0]).order_by(cls.likes.desc()).limit(15).all()

    @classmethod
    def add_views_by_one(cls, query_uid):
        discovered_entry = cls.find_entry_by_uid(query_uid)
        discovered_entry.views += 1
        discovered_entry.create_active_user()

    @classmethod
    def add_likes_by_one(cls, query_uid):
        discovered_entry = cls.find_entry_by_uid(query_uid)
        discovered_entry.likes += 1
        discovered_entry.create_active_user()

    @classmethod
    def reduce_likes_by_one(cls, query_uid):
        discovered_entry = cls.find_entry_by_uid(query_uid)
        discovered_entry.likes -= 1
        discovered_entry.create_active_user()

    @classmethod
    def generate_fresh_uid(cls):
        fresh_uid = cls.generate_random_uid()
        while cls.find_entry_by_uid(fresh_uid) is not None:
            fresh_uid = cls.generate_random_uid()
        return fresh_uid

    @classmethod
    def generate_search_data(cls, active_user_list, current_user):
        active_user_object = cls.find_entry_by_uid(current_user)
        return [
            {
                'uid': active_user.uid,
                'name': active_user.name,
                'image': active_user.basic.image
                if (active_user.basic and active_user.basic.image != 'no-image')
                else NO_IMAGE_AVAILABLE,
                'already_following': active_user.uid in [following.target for following in active_user_object.following]
            } for active_user in active_user_list
        ]

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
