from django import forms
from .models import Contacto, Persona, Direccion

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'