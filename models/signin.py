from db import db


class SignInModel(db.Model):
    email = db.Column(db.VARCHAR(80), primary_key=True)
    password = db.Column(db.VARCHAR(100), nullable=False)
