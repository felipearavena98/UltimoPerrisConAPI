# Generated by Django 2.0.7 on 2018-12-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_lista_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costoPresupuesto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='costoReal',
            field=models.IntegerField(default=0),
        ),
    ]
