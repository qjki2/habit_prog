from app.extensions import ma
from marshmallow import fields, validate
#dump -> Json
#load -> Python object (da json a python) 

class UserSchema(ma.Schema):
    id_U = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))

class HabitSchema(ma.Schema):
    id_H = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(allow_none=True)
    streak = fields.Int(dump_only=True)

class SegueHabitSchema(ma.Schema):
    id_U = fields.Int(required=True)
    id_H = fields.Int(required=True)
    data_inizio = fields.DateTime(dump_only=True) #data generata dal server 

class HabitLogSchema(ma.Schema):
    id_L = fields.Int(dump_only=True)
    id_U = fields.Int(dump_only=True) 
    id_H = fields.Int(required=True)
    data = fields.Date(dump_only=True) #data generata dal server
    completato = fields.Bool(required=True)