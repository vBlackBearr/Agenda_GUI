
# agenda/urls.py
from django.urls import path
from .views import login, home, agenda

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('agenda/', agenda, name='agenda'),
    # Puedes agregar más URLs según sea necesario
]
