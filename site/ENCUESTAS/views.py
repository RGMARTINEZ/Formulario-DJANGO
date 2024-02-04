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
"otra_participacion",
"otro_caracter_confesional",
"otra_vocacion",
"tiene_organizaciones_sector_nombre",
"tiene_organizaciones_sector_direccion",
"tiene_organizaciones_sector_correo",
"tiene_organizaciones_sector_telefono",
"tiene_organizaciones_sector_nit",
"participa_actividades_caridad_departamento",
"participa_actividades_caridad_departamento_otro",
"participa_actividades_carida_municipio",
"participa_actividades_carida_municipio_otro",
"participa_actividades_caridad_localidad",
"participa_actividades_caridad_telefono",
"participa_actividades_caridad_descripcion",
"colabora_proyectos_sociales_telefono",
"colabora_proyectos_sociales_celular",
"colabora_proyectos_sociales_correo",
"colabora_proyectos_sociale_representan",
"ofrece_servicios_poblaciones_otro",
"impacto_comunidad_valores_cuales",
"otra_areas_temas_prioridad",
"otra_principales_inciativas_sociales",
"otra_como_finacia_proyectos",
"tiene_alianzas_ongs_cuales",
"otros_resultados_destacados",
"ofrece_servicios_sociedad",
"ofrece_servicios_sociedad_dificultades",
"ofrece_servicios_sociedad_tecnica",
"ofrece_servicios_sociedad_ciudadana",
"ofrece_servicios_sociedad_lideres",
"ofrece_servicios_sociedad_otra",
"otra_cuales_actividades_ods",
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