# some_app/views.py
from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
    template_name = "encuestas/NiceAdmin/index.html"