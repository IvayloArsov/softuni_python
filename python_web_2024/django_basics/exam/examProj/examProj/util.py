from authors.models import Author


def get_user_obj():
    return Author.objects.first()

class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.add_placeholders()

class ReadOnlyMixin:
    readonly_fields = []
    def make_fields_readonly(self):
        for field_name in self.readonly_fields:
            if field_name in self.readonly_fields:
                self.fields[field_name].widget.attrs['readonly'] = True

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.make_fields_readonly()