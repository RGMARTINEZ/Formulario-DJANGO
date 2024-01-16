from django import forms
from ENCUESTAS.models import Encuesta


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        # Override the rendering to apply form-check-input class
        if attrs is None:
            attrs = {}
        attrs['class'] = 'form-check-input'
        return super().render(name, value, attrs, choices)


fields_to_hidde = {
    "otra_zona_entidad": "otra_zona_entidad",
    "otra_poblacion_entidad": "otra_poblacion_entidad",
    "otros_grupos_personas": "otros_grupos_personas",
    "otra_discapacidad": "otra_discapacidad",
    "otro_idioma": "otro_idioma",
    "otra_actividad": "otra_actividad",
    "otro_servicio": "otro_servicio",
    "otro_caracter_confesional": "otro_caracter_confesional",
    "otros_resultados_destacados": "otros_resultados_destacados",
    "otro_enfoque_principal_servicios": "otro_enfoque_principal_servicios",
    "otros_beneficios_implementado_seguridad": "otros_beneficios_implementado_seguridad"
}

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
            if fields_to_hidde.get(field_name):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['style'] = 'display: none'


