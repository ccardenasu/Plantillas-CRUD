# Generated by Django 5.1 on 2024-10-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0021_alter_datos_cfs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datos",
            name="lan",
            field=models.CharField(default="0.0.0.0/0", max_length=300),
        ),
        migrations.AlterField(
            model_name="datos",
            name="unit_nid",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
