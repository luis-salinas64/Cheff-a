# Generated by Django 3.2.2 on 2022-06-22 01:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheff_app', '0018_auto_20220621_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cpte_nro', models.PositiveIntegerField(default=0, unique=True, verbose_name='cpte_nro')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='fecha')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='precio')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cantidad')),
                ('importe', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='importe')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cheff_app.categoria')),
                ('ingredientes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cheff_app.ingredientes')),
                ('producto_elaborado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cheff_app.productoelaborado')),
                ('producto_terminado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cheff_app.productoterminado')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cheff_app.proveedor')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cheff_app.comprobante')),
            ],
            options={
                'db_table': 'operacion',
            },
        ),
        migrations.DeleteModel(
            name='IngresosMercaderia',
        ),
    ]