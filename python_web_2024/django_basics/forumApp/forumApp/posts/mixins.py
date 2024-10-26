from django.forms import Form


class DisableFieldsMixin(Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if (
                    self.disabled_fields[0] == '__all__'
                    or
                    field_name in self.disabled_fields
            ):
                self.fields[field_name].disabled = True
