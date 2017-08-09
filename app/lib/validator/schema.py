# coding=utf-8


from app.libs.validator.fields import String, Field


class SchemaMetaClass(type):

    def __new__(cls, name, bases, attrs):
        for n, v in attrs.items():
            if isinstance(v, Field):
                v.name = n
        return super(SchemaMetaClass, cls).__new__(cls, name, bases, attrs)


class Schema(object):

    __metaclass__ = SchemaMetaClass

    def __init__(self, data):
        self.data = data

    def validate(self):
        rv = {}
        for field_name in dir(self):
            field = getattr(self, field_name)
            if isinstance(field, Schema):
                rv.update(field.validate())
            else:
                rv[field_name] = field
        return rv


