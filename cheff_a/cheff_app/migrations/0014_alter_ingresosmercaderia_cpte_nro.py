# Generated by Django 3.2.2 on 2022-06-21 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheff_app', '0013_ingresosmercaderia_ingredientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresosmercaderia',
            name='cpte_nro',
            field=models.PositiveIntegerField(default=0, verbose_name='cpte_nro'),
        ),
    ]
