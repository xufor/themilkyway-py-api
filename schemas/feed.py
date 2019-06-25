from marshmallow import Schema, fields


class FeedSchema(Schema):
    version = fields.Integer(required=True, validate=lambda v: 1 <= v <= 5)
