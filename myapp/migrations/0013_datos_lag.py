# Generated by Django 5.1 on 2024-09-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0012_datos_ies"),
    ]

    operations = [
        migrations.AddField(
            model_name="datos",
            name="lag",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]