from db import db
from sqlalchemy.exc import SQLAlchemyError

from models.basic import IS_PRIVATE


ERROR_WRITING_LIKE_TABLE = 'Error writing likes table.'
ERROR_DELETING_LIKE_TABLE = 'Error deleting from likes table.'


class LikesModel(db.Model):

    __tablename__ = 'likes'

    sno = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    source = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'), nullable=False)
    target = db.Column(db.VARCHAR(8), db.ForeignKey('stories.sid'), nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)

    @classmethod
    def generate_favourites_profile_data(cls, active_user_object):
        if active_user_object.basic is not None:
            if active_user_object.basic.private:
                return {'message': IS_PRIVATE}
        if active_user_object.basic is None:
            return [
                {
                    'uid': like.liked.uid,
                    'sid': like.liked.sid,
                    'name': like.liked.author.name,
                    'summary': like.liked.summary,
                    'title': like.liked.title
                } for like in active_user_object.favourites
            ]

    @classmethod
    def force_generate_favourites_profile_data(cls, active_user_object):
        return [
            {
                'uid': like.liked.uid,
                'sid': like.liked.sid,
                'name': like.liked.author.name,
                'summary': like.liked.summary,
                'title': like.liked.title
             } for like in active_user_object.favourites
        ]

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


