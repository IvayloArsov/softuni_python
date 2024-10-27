from django import forms
from authors.models import Author
from examProj.util import PlaceholderMixin


class AuthorBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'passcode', 'pets_number')

class AuthorCreateForm(AuthorBaseForm):
    pass

class AuthorEditForm(AuthorBaseForm):
    pass