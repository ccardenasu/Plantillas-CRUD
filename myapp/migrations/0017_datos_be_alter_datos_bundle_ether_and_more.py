# Generated by Django 5.1 on 2024-09-26 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_remove_datos_administrative_state_remove_datos_nodo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="datos",
            name="be",
            field=models.CharField(default="0", max_length=100),
        ),
        migrations.AlterField(
            model_name="datos",
            name="bundle_ether",
            field=models.CharField(
                choices=[
                    ("N/A", "N/A"),
                    ("Bundle-ether10", "Bundle-ether10"),
                    ("Bundle-ether11", "Bundle-ether11"),
                    ("Bundle-ether12", "Bundle-ether12"),
                    ("Bundle-ether13", "Bundle-ether13"),
                    ("Bundle-ether14", "Bundle-ether14"),
                    ("Bundle-ether32", "Bundle-ether32"),
                    ("Bundle-ether33", "Bundle-ether33"),
                    ("TE7/3", "TE7/3"),
                ],
                default="N/A",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="datos",
            name="bundle_ether_b",
            field=models.CharField(
                choices=[
                    ("N/A", "N/A"),
                    ("Bundle-ether10", "Bundle-ether10"),
                    ("Bundle-ether11", "Bundle-ether11"),
                    ("Bundle-ether12", "Bundle-ether12"),
                    ("Bundle-ether13", "Bundle-ether13"),
                    ("Bundle-ether14", "Bundle-ether14"),
                    ("Bundle-ether32", "Bundle-ether32"),
                    ("Bundle-ether33", "Bundle-ether33"),
                    ("TE7/3", "TE7/3"),
                ],
                default="N/A",
                max_length=100,
            ),
        ),
    ]
