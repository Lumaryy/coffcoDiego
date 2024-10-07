# Generated by Django 5.0.4 on 2024-10-07 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rol', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('correo_electronico', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=128)),
                ('tipo_documento', models.CharField(choices=[('cc', 'Cédula de Ciudadanía'), ('ti', 'Tarjeta de Identidad'), ('nit', 'NIT'), ('pasaporte', 'Pasaporte')], default='cc', max_length=10)),
                ('numero_documento', models.CharField(max_length=20)),
                ('estado', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rol.rol')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
