# Crear un nuevo archivo migrations/0001_initial.py en la carpeta de la aplicación 'direccion'
import django
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('numero_exterior', models.CharField(max_length=10)),
                ('numero_interior', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=100)),
            ],
        ),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]


# Crear un nuevo archivo migrations/0001_initial.py en la carpeta de la aplicación 'contacto'
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.direccion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.persona')),
            ],
        ),
    ]


# Crear un nuevo archivo migrations/0001_initial.py en la carpeta de la aplicación 'invitacion'
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_invitacion', models.CharField(max_length=20)),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.persona')),
            ],
        ),
    ]

