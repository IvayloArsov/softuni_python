from django.core.exceptions import ValidationError


def is_alpha_only(value:str):
    if not value.isalpha():
        raise ValidationError(
            'Fruit name should contain only letters!'
        )