
# Register your models here.
from django.contrib import admin

from ENCUESTAS.models import Encuesta

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ["creado", "nombre_entidad_religiosa", "nombre_persona", "tipo_afiliacion", "zona_entidad_religiosa"]

admin.site.register(Encuesta, EncuestaAdmin)