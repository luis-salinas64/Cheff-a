# Generated by Django 3.2.2 on 2022-07-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheff_app', '0002_alter_ctaprov_debe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctaprov',
            name='haber',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='haber'),
        ),
        migrations.AlterField(
            model_name='ctaprov',
            name='saldo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='saldo'),
        ),
    ]
