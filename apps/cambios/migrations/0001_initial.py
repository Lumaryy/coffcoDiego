# Generated by Django 5.0.4 on 2024-10-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cambios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('estado_cambio', models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('desaprobado', 'Desaprobado')], default='pendiente', max_length=11)),
            ],
        ),
    ]
