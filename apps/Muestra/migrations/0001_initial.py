# Generated by Django 5.0.4 on 2024-09-04 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Finca', '0001_initial'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muestra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_entrada', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fecha_entrada', models.DateField()),
                ('fecha_muestra', models.DateField()),
                ('codigo_muestra', models.CharField(max_length=45)),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finca.finca')),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuarios')),
            ],
        ),
    ]
