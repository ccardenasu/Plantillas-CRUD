from django import forms
from django.core.validators import validate_ipv4_address
from django.core.exceptions import ValidationError
from .models import Datos
import re
import ipaddress


class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = [
            "cfs",
            "tipo_configuracion",
            "tipo_servicio",
            "tipo_equipo",
            "dko",
            "IES",
            "cliente",
            "sede",
            "sede_b",
            "vt",
            "sw",
            "interface_sw",
            "rfs_ip_port",
            "rfs_ip_port_b",
            "sw_b",
            "interface_sw_b",
            "vrf",
            "rd",
            "unit",
            "unit_b",
            "sv",
            "cv",
            "bw",
            "wan",
            "wanv6",
            "asn",
            "lan",
            "lanv6",
            "lbcpe",
            "lnnid",
            "bundle_ether",
            "pe",
            "interface_pe",
            "puertos_lag",
            "lag",
            "bundle_ether_b",
            "pe_b",
            "interface_pe_b",
             "pais",
            "mercado",
        ]
        widgets = {
            "cfs": forms.TextInput(attrs={"class": "form-control"}),
            "bundle_ether": forms.Select(attrs={"class": "form-control"}),
            "bundle_ether_b": forms.Select(attrs={"class": "form-control"}),
            "tipo_configuracion": forms.Select(attrs={"class": "form-control"}),
            "tipo_equipo": forms.Select(attrs={"class": "form-control"}),
            "tipo_servicio": forms.Select(attrs={"class": "form-control"}),
            "rfs_ip_port": forms.TextInput(attrs={"class": "form-control"}),
            "rfs_ip_port_b": forms.TextInput(attrs={"class": "form-control"}),
            "cliente": forms.TextInput(attrs={"class": "form-control"}),
            "sede": forms.TextInput(attrs={"class": "form-control"}),
            "sede_b": forms.TextInput(attrs={"class": "form-control"}),
            "dko": forms.TextInput(attrs={"class": "form-control"}),
            "IES": forms.TextInput(attrs={"class": "form-control"}),
            "sw": forms.TextInput(attrs={"class": "form-control"}),
            "interface_sw": forms.TextInput(attrs={"class": "form-control"}),
            "sw_b": forms.TextInput(attrs={"class": "form-control"}),
            "interface_sw_b": forms.TextInput(attrs={"class": "form-control"}),
            "pe": forms.TextInput(attrs={"class": "form-control"}),
            "interface_pe": forms.TextInput(attrs={"class": "form-control"}),
            "puertos_lag": forms.TextInput(attrs={"class": "form-control"}),
            "lag": forms.TextInput(attrs={"class": "form-control"}),
            "pe_b": forms.TextInput(attrs={"class": "form-control"}),
            "interface_pe_b": forms.TextInput(attrs={"class": "form-control"}),
            "vrf": forms.TextInput(attrs={"class": "form-control"}),
            "rd": forms.TextInput(attrs={"class": "form-control"}),
            "unit": forms.TextInput(attrs={"class": "form-control"}),
            "unit_b": forms.TextInput(attrs={"class": "form-control"}),
            "vt": forms.TextInput(attrs={"class": "form-control"}),
            "sv": forms.TextInput(attrs={"class": "form-control"}),
            "cv": forms.TextInput(attrs={"class": "form-control"}),
            "bw": forms.TextInput(attrs={"class": "form-control"}),
            "wan": forms.TextInput(attrs={"class": "form-control"}),
            "wanv6": forms.TextInput(attrs={"class": "form-control"}),
            "asn": forms.TextInput(attrs={"class": "form-control"}),
            "lan": forms.TextInput(attrs={"class": "form-control"}),
            "lanv6": forms.TextInput(attrs={"class": "form-control"}),
            "lbcpe": forms.TextInput(attrs={"class": "form-control"}),
            "lnnid": forms.TextInput(attrs={"class": "form-control"}),
            "pais": forms.Select(attrs={"class": "form-control"}),
            "mercado": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_cfs(self):
        cfs = self.cleaned_data.get("cfs")
        if not cfs.isdigit():
            raise forms.ValidationError("El campo CFS debe contener solo números.")
        return cfs

    def clean_wan(self):
        wan = self.cleaned_data.get("wan")
        # Validar formato CIDR
        cidr_pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$")
        if not cidr_pattern.match(wan):
            raise ValidationError(
                "La IP WAN no es válida. Por favor, ingresa una dirección IPv4 en formato CIDR, por ejemplo: 192.168.1.1/24"
            )

        # Separar IP y máscara
        ip, mask = wan.split("/")
        try:
            validate_ipv4_address(ip)
        except ValidationError:
            raise ValidationError(
                "La IP WAN no es válida. Por favor, ingresa una dirección IPv4 válida, por ejemplo: 192.168.1.1/24"
            )

        # Validar máscara
        if not (0 <= int(mask) <= 32):
            raise ValidationError(
                "La máscara de red no es válida. Debe estar entre 0 y 32, por ejemplo: 192.168.1.1/24"
            )

        # Calcular la dirección de red
        network = ipaddress.IPv4Network(wan, strict=False)
        network_ip = str(network.network_address)

        # Si la IP no es la dirección de red, actualizarla
        if ip != network_ip:
            self.cleaned_data["wan"] = f"{network_ip}/{mask}"
            raise ValidationError(
                f"La IP de red WAN debería ser la IP de red: {network_ip}/{mask}"
            )

        return wan

    def clean(self):
        cleaned_data = super().clean()
        bw = cleaned_data.get("bw")

        if bw and bw.isdigit():
            cleaned_data["BWx1024"] = int(bw) * 1024
        else:
            raise ValidationError("El campo BW debe contener solo números.")

        return cleaned_data

    def clean_interface_pe(self):
        interface_pe = self.cleaned_data.get("interface_pe")
        match = re.search(r"\d+", interface_pe)
        if match:
            self.cleaned_data["num_puertos_lag"] = match.group()
        else:
            raise ValidationError("No se encontró un número en la interfaz PE.")
        return interface_pe
