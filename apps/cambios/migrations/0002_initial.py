# Generated by Django 5.0.4 on 2024-10-07 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cambios', '0001_initial'),
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambios',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio.servicio'),
        ),
    ]
