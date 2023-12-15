from django.contrib import admin

# Register your models here.
from .models import Persona, Contacto, Direccion, Invitaciones

# Register your models here.
admin.site.register(Persona)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Invitaciones)
