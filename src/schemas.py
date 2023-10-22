"""
class TrainingSchema(ma.Schema):
    _id = fields.fields.Integer()
    name = fields.fields.Str()
    date = fields.fields.DateTime(format='%Y-%m-%d')
    duration = fields.fields.Integer()
    note = fields.fields.Str()
"""
from src import ma
from flask_marshmallow import fields


class NotesSchema(ma.Schema):
    id = fields.fields.Integer()
    date = fields.fields.DateTime(format='%Y-%m-%d')
    content = fields.fields.Str()
    author = fields.fields.Str()
