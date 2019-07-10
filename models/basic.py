from sqlalchemy.exc import SQLAlchemyError

from db import db

NO_IMAGE_AVAILABLE = 'No Image available.'
ERROR_WRITING_BASIC_TABLE = 'Error writing basic table.'
IS_PRIVATE = 'The author has decided not to show his private details.'


class BasicModel(db.Model):

    __tablename__ = 'basic'

    sno = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    uid = db.Column(db.VARCHAR(6), db.ForeignKey('active.uid'), nullable=False)
    dob = db.Column(db.DATE, nullable=False)
    bio = db.Column(db.VARCHAR(500), nullable=False)
    country = db.Column(db.VARCHAR(60), nullable=False)
    profession = db.Column(db.VARCHAR(20), nullable=False)
    image = db.Column(db.VARCHAR(50), nullable=False)
    private = db.Column(db.BOOLEAN, nullable=False)
    preferences = db.Column(db.VARCHAR(100), nullable=False)

    @classmethod
    def generate_basic_profile_data(cls, active_user_object):
        if active_user_object.basic is None:
            return {
                'message': 'No data',
                'name': active_user_object.name,
                'image': NO_IMAGE_AVAILABLE
            }
        elif active_user_object.basic.private:
            return {'message': IS_PRIVATE}
        return {
            'bio': active_user_object.basic.bio,
            'country': active_user_object.basic.country,
            'email': active_user_object.basic.strong.email,
            'profession': active_user_object.basic.profession,
            'dob': str(active_user_object.basic.dob),
            'preferences': active_user_object.preferences,
            'image': active_user_object.basic.image
            if active_user_object.basic.image != 'no-image'
            else NO_IMAGE_AVAILABLE,
            'name': active_user_object.name,
        }

    @classmethod
    def force_generate_basic_profile_data(cls, active_user_object):
        if active_user_object.basic is None:
            return {
                'message': 'No data',
                'name': active_user_object.name,
                'image': NO_IMAGE_AVAILABLE
            }
        return {
            'bio': active_user_object.basic.bio,
            'country': active_user_object.basic.country,
            'email': active_user_object.email,
            'name': active_user_object.name,
            'preferences': active_user_object.preferences,
            'image': active_user_object.basic.image
            if active_user_object.basic.image != 'no-image'
            else NO_IMAGE_AVAILABLE,
            'profession': active_user_object.basic.profession,
            'dob': str(active_user_object.basic.dob),
        }

    def create_entry(self):
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ERROR_WRITING_BASIC_TABLE

