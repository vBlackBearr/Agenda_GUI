
# agenda/urls.py
from django.urls import path
from .views import login, home, agenda, formulario_contacto, crear_contacto, crear_contacto_exitoso, editar_contacto

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('agenda/', agenda, name='agenda'),
    path('formulario_contacto/', formulario_contacto, name='formulario_contacto'),
    path('crear_contacto/', crear_contacto, name='crear_contacto'),
    path('crear_contacto_exitoso/', crear_contacto_exitoso, name='crear_contacto_exitoso'),
    path('editar_contacto/<int:contacto_id>/', editar_contacto, name='editar_contacto'),
]
