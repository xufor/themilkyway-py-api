from marshmallow import Schema, fields


class SigninSchema(Schema):
    email = fields.Email(required=True, validate=lambda e: 1 <= len(e) <= 80)
    password = fields.String(required=True, validate=lambda e: 1 <= len(e) <= 72)
