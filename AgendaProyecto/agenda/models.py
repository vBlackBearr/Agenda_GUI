from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Direccion(models.Model):
    ciudad = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10, null=True, blank=True)
    colonia = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ciudad}, {self.colonia}"


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    ap_paterno = models.CharField(max_length=255)
    ap_materno = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.ap_paterno} {self.ap_materno}"


class Contacto(models.Model):
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.persona} - {self.direccion}"


class Invitaciones(models.Model):
    remitente = models.CharField(max_length=255)
    tipo_invitacion = models.IntegerField()

    def __str__(self):
        return f"Remitente: {self.remitente}, Tipo de Invitación: {self.tipo_invitacion}"
