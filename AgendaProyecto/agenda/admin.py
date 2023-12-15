from django.contrib import admin

# Register your models here.
from .models import Persona, Contacto, Direccion, Invitaciones, Correo, Telefono

# Register your models here.
admin.site.register(Persona)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Invitaciones)
admin.site.register(Correo)
admin.site.register(Telefono)
