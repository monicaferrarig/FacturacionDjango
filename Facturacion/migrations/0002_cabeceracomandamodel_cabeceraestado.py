# Generated by Django 3.1.6 on 2021-02-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabeceracomandamodel',
            name='cabeceraEstado',
            field=models.CharField(db_column='cabecera_estado', default='ABIERTO', max_length=50, verbose_name='Estado del Pedido'),
        ),
    ]
