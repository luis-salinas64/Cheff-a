# Generated by Django 3.2.2 on 2022-06-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheff_app', '0011_auto_20220621_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresosmercaderia',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='stock'),
        ),
    ]
