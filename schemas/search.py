from marshmallow import Schema, fields


class SearchSchema(Schema):
    # The query string cannot be greater than length 5
    name = fields.String(required=True, validate=lambda e: 5 <= len(e) <= 80)
    version = fields.Integer(required=True, validate=lambda v: 1 <= v <= 10)
