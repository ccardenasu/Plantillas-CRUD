# Generated by Django 5.1 on 2024-09-08 02:11

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
                            ("Bundle-ether10", "Bundle-ether10"),
                            ("Bundle-ether11", "Bundle-ether11"),
                            ("Bundle-ether12", "Bundle-ether12"),
                            ("Bundle-ether13", "Bundle-ether13"),
                            ("Bundle-ether14", "Bundle-ether14"),
                            ("Bundle-ether32", "Bundle-ether32"),
                            ("Bundle-ether33", "Bundle-ether33"),
                        ],
                        default="Bundle-ether10",
                        max_length=100,
                    ),
                ),
                ("cfs", models.CharField(max_length=100)),
                (
                    "tipo_configuracion",
                    models.CharField(
                        choices=[
                            ("ampliacion_VPN_Jun", "Ampliacion VPN Jun"),
                            ("Ampliacion_ADI_Alcatel", "Ampliacion ADI Alcatel"),
                            ("BGP_VPN_Jun", "BGP VPN Jun"),
                            ("Ampliacion_ADI_Juniper", "Ampliacion ADI Juniper"),
                            (
                                "Ampliacion_ADI_Alcatel_XCON",
                                "Ampliacion ADI Alcatel XCON",
                            ),
                            (
                                "Ampliacion_ADI_Alcatel_VPL",
                                "Ampliacion ADI Alcatel VPL",
                            ),
                            ("Ampliacion_VPLS_Juniper", "Ampliacion VPLS Juniper"),
                            ("Instalacion_VPN_Juniper", "Instalacion VPN Juniper"),
                            ("Instalacion_ADI_Alcatel", "Instalacion ADI Alcatel"),
                            ("Instalacion_ADI_Juniper", "Instalacion ADI Juniper"),
                            (
                                "Instalacion_ADI_Alcatel_VPL",
                                "Instalacion ADI Alcatel VPL",
                            ),
                            (
                                "Instalacion_ADI_Alcatel_Xco",
                                "Instalacion ADI Alcatel Xco",
                            ),
                            ("Instalacion_VPLS_Juniper", "Instalacion VPLS Juniper"),
                            ("Instalacion_ADI_JUN_XCON", "Instalacion ADI JUN XCON"),
                            ("Instalacion_ADI_irs", "Instalacion ADI irs"),
                            ("Instalacion_VPLS_J_p2p", "Instalacion VPLS J p2p"),
                            (
                                "Instalacion_NNI_VRF_GRIS_AZ",
                                "Instalacion NNI VRF GRIS AZ",
                            ),
                        ],
                        default="default_config",
                        max_length=100,
                    ),
                ),
                (
                    "tipo_servicio",
                    models.CharField(
                        choices=[("VPN", "VPN"), ("VPLS", "VPLS"), ("ADI", "ADI")],
                        default="VPN",
                        max_length=100,
                    ),
                ),
                (
                    "rfs_ip_port",
                    models.CharField(default="default_rfs_ip_port", max_length=100),
                ),
                (
                    "cliente",
                    models.CharField(default="default_cliente", max_length=100),
                ),
                ("sede", models.CharField(default="default_sede", max_length=100)),
                ("dko", models.CharField(max_length=100)),
                ("sw", models.CharField(max_length=100)),
                ("interface_sw", models.CharField(max_length=100)),
                ("pe", models.CharField(max_length=100)),
                ("interface_pe", models.CharField(max_length=100)),
                ("vrf", models.CharField(max_length=100)),
                ("rd", models.CharField(max_length=100)),
                ("unit", models.CharField(max_length=100)),
                ("vt", models.CharField(blank=True, max_length=100, null=True)),
                ("sv", models.CharField(max_length=100)),
                ("cv", models.CharField(blank=True, max_length=100, null=True)),
                ("bw", models.CharField(max_length=100)),
                ("wan", models.CharField(max_length=100)),
                ("wanv6", models.CharField(blank=True, max_length=100, null=True)),
                ("asn", models.CharField(max_length=100)),
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
