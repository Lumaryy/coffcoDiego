# Generated by Django 5.0.4 on 2024-10-07 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TipoServicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_precio', models.BooleanField(default=True)),
                ('presentacion', models.CharField(max_length=45)),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('unidad_medida', models.CharField(choices=[('Lb', 'Libra'), ('Kg', 'Kilogramo')], default='Lb', max_length=2)),
                ('tiposervicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TipoServicio.tiposervicio')),
            ],
        ),
    ]
