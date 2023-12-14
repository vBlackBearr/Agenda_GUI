
# agenda/urls.py
from django.urls import path
from .views import login, home

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    # Puedes agregar más URLs según sea necesario
]
