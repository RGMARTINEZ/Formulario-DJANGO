from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ENCUESTAS.models import Encuesta
from ENCUESTAS.forms import EncuestaModelForm


class PaginaInicial(TemplateView):
    template_name = "encuestas/base.html"



fields_to_hidde = [
    "otra_zona_entidad",
    "otra_poblacion_entidad",
    "otros_grupos_personas",
    "otra_discapacidad",
    "otro_idioma",
    "otra_actividad",
    "otro_servicio",
    "otro_caracter_confesional",
    "otros_resultados_destacados",
    "otro_enfoque_principal_servicios",
    "otros_beneficios_implementado_seguridad"
]


class FormularioCreateModelView(CreateView):
    model = Encuesta
    form_class = EncuestaModelForm
    template_name = 'encuestas/formulario.html'
    success_url = reverse_lazy('success_url')  # Redirect to a success page

    def get_context_data(self, **kwargs):
        context = super(FormularioCreateModelView, self).get_context_data(**kwargs)

        # Add additional context data here
        context['fields_to_hidde'] = fields_to_hidde

        return context