from marshmallow import Schema, fields


class SearchSchema(Schema):
    # The query string cannot be less than length 5
    string = fields.String(required=True, validate=lambda e: 5 <= len(e) <= 100)
    version = fields.Integer(required=True, validate=lambda v: 1 <= v <= 10)
    content = fields.String(required=True, validate=lambda c: c in ['stories', 'authors'])
