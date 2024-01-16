from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ENCUESTAS.models import Encuesta
from ENCUESTAS.forms import EncuestaModelForm


class PaginaInicial(TemplateView):
    template_name = "encuestas/base.html"


class FormularioCreateModelView(CreateView):
    model = Encuesta
    form_class = EncuestaModelForm
    template_name = 'encuestas/formulario.html'
    success_url = reverse_lazy('success_url')  # Redirect to a success page