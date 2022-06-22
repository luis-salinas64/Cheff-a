# Generated by Django 3.2.2 on 2022-06-21 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheff_app', '0010_ingresosmercaderia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresosmercaderia',
            name='producto',
        ),
        migrations.AddField(
            model_name='ingresosmercaderia',
            name='producto_elaborado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cheff_app.productoelaborado'),
        ),
        migrations.AddField(
            model_name='ingresosmercaderia',
            name='producto_terminado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cheff_app.productoterminado'),
        ),
    ]
