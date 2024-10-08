# Generated by Django 5.1 on 2024-09-09 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Datos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bundle_ether",
                    models.CharField(
                        choices=[
                            ("N/A", "N/A"),
                            ("Bundle-ether10", "Bundle-ether10"),
                            ("Bundle-ether11", "Bundle-ether11"),
                            ("Bundle-ether12", "Bundle-ether12"),
                            ("Bundle-ether13", "Bundle-ether13"),
                            ("Bundle-ether14", "Bundle-ether14"),
                            ("Bundle-ether32", "Bundle-ether32"),
                            ("Bundle-ether33", "Bundle-ether33"),
                        ],
                        default="N/A",
                        max_length=100,
                    ),
                ),
                ("cfs", models.CharField(max_length=100)),
                (
                    "tipo_configuracion",
                    models.CharField(
                        choices=[
                            ("", ""),
                            ("Ampliacion", "Ampliacion"),
                            ("BGP", "BGP"),
                            ("Alta", "Alta"),
                        ],
                        default="default_config",
                        max_length=100,
                    ),
                ),
                (
                    "tipo_servicio",
                    models.CharField(
                        choices=[
                            ("", ""),
                            ("VPN", "VPN"),
                            ("VPLS", "VPLS"),
                            ("ADI", "ADI"),
                        ],
                        default="",
                        max_length=100,
                    ),
                ),
                (
                    "rfs_ip_port",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("cliente", models.CharField(blank=True, max_length=100, null=True)),
                ("sede", models.CharField(blank=True, max_length=100, null=True)),
                ("dko", models.CharField(blank=True, max_length=100, null=True)),
                ("sw", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "interface_sw",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("swb", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "interface_swb",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("pe", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "interface_pe",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("vrf", models.CharField(blank=True, max_length=100, null=True)),
                ("rd", models.CharField(blank=True, max_length=100, null=True)),
                ("unit", models.CharField(blank=True, max_length=100, null=True)),
                ("vt", models.CharField(blank=True, max_length=100, null=True)),
                ("sv", models.CharField(blank=True, max_length=100, null=True)),
                ("cv", models.CharField(blank=True, max_length=100, null=True)),
                ("bw", models.CharField(blank=True, max_length=100, null=True)),
                ("wan", models.CharField(default="0.0.0.0/0", max_length=100)),
                ("wanv6", models.CharField(blank=True, max_length=100, null=True)),
                ("asn", models.CharField(blank=True, max_length=100, null=True)),
                ("lan", models.CharField(blank=True, max_length=100, null=True)),
                ("lbcpe", models.CharField(blank=True, max_length=100, null=True)),
                ("lnnid", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Dato",
                "verbose_name_plural": "Datos",
            },
        ),
    ]
