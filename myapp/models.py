from django.db import models
from django.utils import timezone
import pytz

class Datos(models.Model):
    TIPO_CONFIGURACION_CHOICES = [
        ('ampliacion_VPN_Jun', 'Ampliacion VPN Jun'),
        ('Ampliacion_ADI_Alcatel', 'Ampliacion ADI Alcatel'),
        ('BGP_VPN_Jun', 'BGP VPN Jun'),
        ('Ampliacion_ADI_Juniper', 'Ampliacion ADI Juniper'),
        ('Ampliacion_ADI_Alcatel_XCON', 'Ampliacion ADI Alcatel XCON'),
        ('Ampliacion_ADI_Alcatel_VPL', 'Ampliacion ADI Alcatel VPL'),
        ('Ampliacion_VPLS_Juniper', 'Ampliacion VPLS Juniper'),
        ('Instalacion_VPN_Juniper', 'Instalacion VPN Juniper'),
        ('Instalacion_ADI_Alcatel', 'Instalacion ADI Alcatel'),
        ('Instalacion_ADI_Juniper', 'Instalacion ADI Juniper'),
        ('Instalacion_ADI_Alcatel_VPL', 'Instalacion ADI Alcatel VPL'),
        ('Instalacion_ADI_Alcatel_Xco', 'Instalacion ADI Alcatel Xco'),
        ('Instalacion_VPLS_Juniper', 'Instalacion VPLS Juniper'),
        ('Instalacion_ADI_JUN_XCON', 'Instalacion ADI JUN XCON'),
        ('Instalacion_ADI_irs', 'Instalacion ADI irs'),
        ('Instalacion_VPLS_J_p2p', 'Instalacion VPLS J p2p'),
        ('Instalacion_NNI_VRF_GRIS_AZ', 'Instalacion NNI VRF GRIS AZ'),
    ]

    TIPO_SERVICIO_CHOICES = [
        ('VPN', 'VPN'),
        ('VPLS', 'VPLS'),
        ('ADI', 'ADI'),
    ]

    BUNDLE_ETHER_CHOICES = [
        ('Bundle-ether10', 'Bundle-ether10'),
        ('Bundle-ether11', 'Bundle-ether11'),
        ('Bundle-ether12', 'Bundle-ether12'),
        ('Bundle-ether13', 'Bundle-ether13'),
        ('Bundle-ether14', 'Bundle-ether14'),
        ('Bundle-ether32', 'Bundle-ether32'),
        ('Bundle-ether33', 'Bundle-ether33'),
    ]

    bundle_ether = models.CharField(max_length=100, choices=BUNDLE_ETHER_CHOICES, default='Bundle-ether10')
    cfs = models.CharField(max_length=100)
    tipo_configuracion = models.CharField(max_length=100, choices=TIPO_CONFIGURACION_CHOICES, default='default_config')
    tipo_servicio = models.CharField(max_length=100, choices=TIPO_SERVICIO_CHOICES, default='VPN')
    rfs_ip_port = models.CharField(max_length=100, default='default_rfs_ip_port')
    cliente = models.CharField(max_length=100, default='default_cliente')
    sede = models.CharField(max_length=100, default='default_sede')
    dko = models.CharField(max_length=100)
    sw = models.CharField(max_length=100)
    interface_sw = models.CharField(max_length=100)
    pe = models.CharField(max_length=100)
    interface_pe = models.CharField(max_length=100)
    vrf = models.CharField(max_length=100)
    rd = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    vt = models.CharField(max_length=100, blank=True, null=True)
    sv = models.CharField(max_length=100)
    cv = models.CharField(max_length=100, blank=True, null=True)
    bw = models.CharField(max_length=100)
    wan = models.CharField(max_length=100)
    wanv6 = models.CharField(max_length=100, blank=True, null=True)
    asn = models.CharField(max_length=100)
    lan = models.CharField(max_length=100, blank=True, null=True)
    lbcpe = models.CharField(max_length=100, blank=True, null=True)
    lnnid = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        colombia_tz = pytz.timezone('America/Bogota')
        self.created_at = timezone.now().astimezone(colombia_tz)
        super(Datos, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"

    def __str__(self):
        return self.cfs
