from django import forms
from ENCUESTAS.models import Encuesta


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        # Override the rendering to apply form-check-input class
        if attrs is None:
            attrs = {}
        attrs['class'] = 'form-check-input'
        return super().render(name, value, attrs, choices)


class EncuestaModelForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EncuestaModelForm, self).__init__(*args, **kwargs)

        # Apply form-control class to all form fields
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxSelectMultiple):
              field.widget.attrs['class'] = 'form-control'
