# Generated by Django 4.1.2 on 2023-10-31 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Auto',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='Estacionamiento',
        ),
        migrations.DeleteModel(
            name='TipoCliente',
        ),
    ]
