from django.contrib import admin
from django.urls import include, path
from ENCUESTAS.views import FormularioCreateModelView

urlpatterns = [
    path("formulario/", FormularioCreateModelView.as_view(), name='crear_formulario'),
]
