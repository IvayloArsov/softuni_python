from django.core.exceptions import ValidationError

class AlphabeticValidator:
    def __init__(self, message="Your name must contain letters only!"):
        self.message = message

    def __call__(self, value, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)
