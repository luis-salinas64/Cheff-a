# Generated by Django 3.2.2 on 2022-06-20 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheff_app', '0007_auto_20220620_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stock', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('un_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cheff_app.unmedida')),
            ],
            options={
                'db_table': 'ingredientes',
            },
        ),
    ]
