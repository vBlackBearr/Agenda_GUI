from django.shortcuts import render, redirect, get_object_or_404
from .models import Direccion, Persona, Contacto, Telefono, Correo
from .forms import ContactoForm, PersonaForm, DireccionForm


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def agenda(request):
    # Obtén todos los contactos de la base de datos
    contactos = Contacto.objects.all()

    # Pasa los contactos al contexto del template
    context = {
        'contactos': contactos,
    }

    # Renderiza la plantilla con el contexto
    return render(request, 'agenda.html', context)


def formulario_contacto(request):
    return render(request, 'formulario_contacto.html')


def crear_contacto(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        ciudad = request.POST.get('ciudad')
        codigo_postal = request.POST.get('codigo_postal')
        numero_exterior = request.POST.get('numero_exterior')
        numero_interior = request.POST.get('numero_interior')
        colonia = request.POST.get('colonia')

        nombre = request.POST.get('nombre')
        ap_paterno = request.POST.get('ap_paterno')
        ap_materno = request.POST.get('ap_materno')

        # Crear la dirección
        direccion = Direccion.objects.create(
            ciudad=ciudad,
            codigo_postal=codigo_postal,
            numero_exterior=numero_exterior,
            numero_interior=numero_interior,
            colonia=colonia
        )

        # Crear la persona
        persona = Persona.objects.create(
            nombre=nombre,
            ap_paterno=ap_paterno,
            ap_materno=ap_materno
        )

        # Agregar correos y teléfonos a la persona
        correos = request.POST.getlist('correos[]')
        telefonos = request.POST.getlist('telefonos[]')

        for correo in correos:
            Correo.objects.create(persona=persona, correo=correo)

        for telefono in telefonos:
            Telefono.objects.create(persona=persona, telefono=telefono)

        # Crear el contacto asociando la dirección y la persona
        contacto = Contacto.objects.create(
            direccion=direccion,
            persona=persona
        )

        # Redirigir a la página de éxito o a donde desees
        return redirect('crear_contacto_exitoso')

    # Si no es una solicitud POST, renderizar el formulario
    return render(request, 'crear_contacto.html')


def crear_contacto_exitoso(request):
    return render(request, 'crear_contacto_exitoso.html')


def editar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, pk=contacto_id)
    persona_form = PersonaForm(instance=contacto.persona)
    direccion_form = DireccionForm(instance=contacto.direccion)

    if request.method == 'POST':
        persona_form = PersonaForm(request.POST, instance=contacto.persona)
        direccion_form = DireccionForm(request.POST, instance=contacto.direccion)

        if persona_form.is_valid() and direccion_form.is_valid():
            persona_form.save()
            direccion_form.save()
            return redirect('agenda')

    context = {
        'persona_form': persona_form,
        'direccion_form': direccion_form,
    }

    return render(request, 'editar_contacto.html', context)


def merge(request):
    contactos = Contacto.objects.all()

    context = {'contactos': contactos}
    return render(request, 'merge.html', context)


def merge_contacto_seleccionado(request, contacto_id):
    print("Merge ", contacto_id)
    return redirect('agenda')
