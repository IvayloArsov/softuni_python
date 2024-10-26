import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class AlphaNumValidator:
    PATTERN = r'^[a-zA-Z0-9_]+$'

    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Ensure this value contains only letters, numbers, and underscore."
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        # if not re.match(self.PATTERN, value):
        #     raise ValidationError(self.message)
        if '-' in value or value.lower() != slugify(value):
            raise ValidationError(self.message)
