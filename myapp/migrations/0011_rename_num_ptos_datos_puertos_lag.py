# Generated by Django 5.1 on 2024-09-11 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_datos_num_ptos_alter_datos_tipo_equipo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="datos",
            old_name="num_ptos",
            new_name="puertos_lag",
        ),
    ]
