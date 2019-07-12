from marshmallow import Schema, fields


class ResetSchema(Schema):
    email = fields.Email(required=True)
