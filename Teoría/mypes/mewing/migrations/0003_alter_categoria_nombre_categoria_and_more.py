# Generated by Django 5.0.6 on 2024-06-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mewing', '0002_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre_categoria',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
