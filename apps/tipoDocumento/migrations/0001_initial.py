# Generated by Django 5.0.4 on 2024-09-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDocumento', models.CharField(max_length=45)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
