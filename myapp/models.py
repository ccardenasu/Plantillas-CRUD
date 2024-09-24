from django.db import models
from django.utils import timezone
import pytz


class Datos(models.Model):
    TIPO_CONFIGURACION_CHOICES = [
        ("", ""),
        ("Ampliacion", "Ampliacion"),
        ("BGP", "BGP"),
        ("Alta", "Alta"),
        ("Modificacion", "Modificacion"),
    ]

    TIPO_SERVICIO_CHOICES = [
        ("", ""),
        ("VPN", "VPN"),
        ("VPLS", "VPLS"),
        ("ADI", "ADI"),
    ]

    TIPO_EQUIPO_CHOICES = [
        ("", ""),
        ("JUNIPER", "JUNIPER"),
        ("ALCATEL", "ALCATEL"),
        ("CISCO", "CISCO"),
    ]
    BUNDLE_ETHER_CHOICES = [
        ("N/A", "N/A"),
        ("Bundle-ether10", "Bundle-ether10"),
        ("Bundle-ether11", "Bundle-ether11"),
        ("Bundle-ether12", "Bundle-ether12"),
        ("Bundle-ether13", "Bundle-ether13"),
        ("Bundle-ether14", "Bundle-ether14"),
        ("Bundle-ether32", "Bundle-ether32"),
        ("Bundle-ether33", "Bundle-ether33"),
    ]

    bundle_ether = models.CharField(
        max_length=100, choices=BUNDLE_ETHER_CHOICES, default="N/A"
    )
    bundle_ether_b = models.CharField(
        max_length=100, choices=BUNDLE_ETHER_CHOICES, default="N/A"
    )
    cfs = models.CharField(max_length=100)
    tipo_configuracion = models.CharField(
        max_length=100, choices=TIPO_CONFIGURACION_CHOICES, default="default_config"
    )
    tipo_servicio = models.CharField(
        max_length=100, choices=TIPO_SERVICIO_CHOICES, default=""
    )
    tipo_equipo = models.CharField(
        max_length=100, choices=TIPO_EQUIPO_CHOICES, default=""
    )
    rfs_ip_port = models.CharField(max_length=100, blank=True, null=True)
    rfs_ip_port_b = models.CharField(max_length=100, blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    sede = models.CharField(max_length=100, blank=True, null=True)
    sede_b = models.CharField(max_length=100, blank=True, null=True)
    dko = models.CharField(max_length=100, blank=True, null=True)
    IES = models.CharField(max_length=100, blank=True, null=True)
    sw = models.CharField(max_length=100, blank=True, null=True)
    interface_sw = models.CharField(max_length=100, blank=True, null=True)
    sw_b = models.CharField(max_length=100, blank=True, null=True)
    interface_sw_b = models.CharField(max_length=100, blank=True, null=True)
    pe = models.CharField(max_length=100, blank=True, null=True)
    interface_pe = models.CharField(max_length=100, blank=True, null=True)
    puertos_lag = models.CharField(max_length=100, default="1")
    lag = models.CharField(max_length=100, blank=True, null=True)
    pe_b = models.CharField(max_length=100, blank=True, null=True)
    interface_pe_b = models.CharField(max_length=100, blank=True, null=True)
    vrf = models.CharField(max_length=100, blank=True, null=True)
    rd = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=100, blank=True, null=True)
    unit_b = models.CharField(max_length=100, blank=True, null=True)
    vt = models.CharField(max_length=100, blank=True, null=True)
    sv = models.CharField(max_length=100, blank=True, null=True)
    cv = models.CharField(max_length=100, blank=True, null=True)
    bw = models.CharField(max_length=100, default="0")
    wan = models.CharField(max_length=100, default="0.0.0.0/0")
    wanv6 = models.CharField(max_length=100, blank=True, null=True)
    asn = models.CharField(max_length=100, blank=True, null=True)
    lan = models.CharField(max_length=100, default="0.0.0.0/0")
    lanv6 = models.CharField(max_length=100, blank=True, null=True)
    lbcpe = models.CharField(max_length=100, blank=True, null=True)
    lnnid = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        colombia_tz = pytz.timezone("America/Bogota")
        self.created_at = timezone.now().astimezone(colombia_tz)
        super(Datos, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"

    def __str__(self):
        return self.cfs
