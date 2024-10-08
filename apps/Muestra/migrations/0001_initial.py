# Generated by Django 5.0.4 on 2024-10-07 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Finca', '0001_initial'),
        ('TipoServicio', '0001_initial'),
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
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('terminado', 'Terminado')], default='pendiente', max_length=9)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('variedad', models.CharField(max_length=45)),
                ('observaciones', models.CharField(blank=True, max_length=255, null=True)),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finca.finca')),
                ('fk_idTipoServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TipoServicio.tiposervicio')),
            ],
        ),
    ]
