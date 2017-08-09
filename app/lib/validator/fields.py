# coding=utf-8


from app.libs.validator.utils import (
    get_function
)
from app.libs.validator.validate import IDCardNumberValidator
from app.exceptions import (
    RespMissingArg, RespBadArg, RespUnauthorizedDenied,
    RespInvalidImageFormat, RespInvalidImageSize
)
from config import MAX_IMAGE_SIZE, MAX_IMAGE_EDGE


class Field(object):
    def __init__(self, default=None, required=True, validate=None, authenticate=None):
        self.name = None
        self.default = default
        self.required = required
        self.validate = validate
        self.authenticate = authenticate
        self.validators = []

    def __get__(self, instance, owner=None):

        if self.validate:
            validate_func = get_function(instance, self.validate)
            self.validators.append(validate_func)

        v = self.get_value(instance)

        if v is None:
            if self.required:
                raise RespMissingArg(self.name)
            v = self.default
        else:
            for validator in self.validators:
                if not validator(v):
                    raise RespBadArg(self.name)

        if self.authenticate:
            authenticate_func = get_function(instance, self.authenticate)
            if not authenticate_func(v):
                raise RespUnauthorizedDenied()
        self.set_value(instance, v)
        return v

    def get_value(self, instance):
        return instance.data.get(self.name)

    def set_value(self, instance, value):
        instance.data[self.name] = value


class String(Field):
    def __init__(self, *args, **kwargs):
        super(String, self).__init__(*args, **kwargs)
        self.validators.insert(0, lambda value: isinstance(value, basestring))


class Int(Field):
    def __init__(self, *args, **kwargs):
        super(Int, self).__init__(*args, **kwargs)
        self.validators.insert(0, lambda value: isinstance(value, (int, long)))

    def get_value(self, instance):
        v = super(Int, self).get_value(instance)
        if v is not None:
            try:
                v = int(v)
            except:
                raise RespBadArg(self.name)
        return v


class IDCardNumber(String):
    def __init__(self, *args, **kwargs):
        super(IDCardNumber, self).__init__(*args, **kwargs)
        self.validators.append(IDCardNumberValidator())


class SchemaType(Field):
    def __init__(self, mapping, depends_on=None):
        super(SchemaType, self).__init__()
        self.mapping = mapping
        self.depends_on = depends_on

    def __get__(self, instance, owner=None):
        if self.depends_on in instance.data:
            cmp_type = instance.data[self.depends_on]
        child_schema_cls = self.mapping[cmp_type]
        return child_schema_cls(instance.data)
