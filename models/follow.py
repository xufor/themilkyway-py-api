from db import db
from sqlalchemy.exc import SQLAlchemyError

from models.basic import IS_PRIVATE

ERROR_WRITING_FOLLOW_TABLE = 'Error writing follow table.'
ERROR_DELETING_FOLLOW_TABLE = 'Error deleting from follow table.'

NO_IMAGE_AVAILABLE = 'No Image available.'


class FollowModel(db.Model):

    __tablename__ = 'follow'

    sno = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    source = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'), nullable=False)
    target = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'), nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)

    @classmethod
    def generate_following_profile_data(cls, active_user_object):
        if active_user_object.basic is not None:
            if active_user_object.basic.private:
                return {'message': IS_PRIVATE}
        if active_user_object.basic is None:
            return [
                {
                    'uid': following.target,
                    'name': following.following.name,
                    'image': following.following.basic.image
                    if (following.following.basic and following.following.basic.image != 'no-image')
                    else NO_IMAGE_AVAILABLE
                } for following in active_user_object.following]

    @classmethod
    def force_generate_following_profile_data(cls, active_user_object):
        return [
            {
                'uid': following.target,
                'name': following.following.name,
                'image': following.following.basic.image
                if (following.following.basic and following.following.basic.image != 'no-image')
                else NO_IMAGE_AVAILABLE
            } for following in active_user_object.following
        ]

    @classmethod
    def generate_followers_profile_data(cls, active_user_object):
        return [
            {
                'uid': followers.source,
                'name': followers.followers.name,
                'image': followers.followers.basic.image
                if (followers.followers.basic and followers.followers.basic.image != 'no-image')
                else NO_IMAGE_AVAILABLE
            } for followers in active_user_object.followers
        ]

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


