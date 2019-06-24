from marshmallow import Schema, fields
from resources.profile import genres


class GenreSchema(Schema):
    genre = fields.String(required=True, validate=lambda g: g in genres)
    version = fields.Integer(required=True, validate=lambda v: 1 <= v <= 10)
