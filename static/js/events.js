import { updateFieldVisibility, updateBundleOptions } from './fieldsToShow.js';
import { buscarCfs, buscarEnCSV, buscarEnCSV_b, concatenar, concatenar_b, concatenar_tipo_servicio_sw } from './functions.js';

export function initializeEventListeners() {
    var tipoServicioField = document.getElementById('id_tipo_servicio');
    var tipoEquipoField = document.getElementById('id_tipo_equipo');
    var tipoConfiguracionField = document.getElementById('id_tipo_configuracion');
    var swField = document.getElementById('id_sw');
    var vrfField = document.getElementById('id_vrf');
    var vrf2Field = document.getElementById('id_vrf2');

    tipoServicioField.addEventListener('change', updateFieldVisibility);
    tipoServicioField.addEventListener('change', updateBundleOptions);
    tipoServicioField.addEventListener('blur', updateFieldVisibility);

    tipoEquipoField.addEventListener('change', updateFieldVisibility);
    tipoEquipoField.addEventListener('blur', updateFieldVisibility);

    tipoConfiguracionField.addEventListener('change', updateFieldVisibility);
    tipoConfiguracionField.addEventListener('change', updateBundleOptions);
    tipoConfiguracionField.addEventListener('blur', updateFieldVisibility);

    if (swField) {
        swField.addEventListener('change', concatenar_tipo_servicio_sw);
        swField.addEventListener('blur', concatenar_tipo_servicio_sw);
    }

    vrfField.addEventListener('blur', function() {
        var vrfValue = vrfField.value;
        if (vrfValue) {
            fetch(`/buscar_vrf_rd/?vrf=${vrfValue}`)
                .then(response => response.json())
                .then(data => {
                    if (data.found) {
                        document.getElementById('id_rd').value = data.rd;
                    } else {
                        document.getElementById('id_rd').value = '';
                        alert("No se encontró el valor de RD para el VRF ingresado.");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert("Ocurrió un error al buscar el valor de RD.");
                });
        }
    });

    vrf2Field.addEventListener('blur', function() {
        var vrf2Value = vrf2Field.value;
        if (vrf2Value) {
            fetch(`/buscar_vrf_rd/?vrf=${vrf2Value}`)
                .then(response => response.json())
                .then(data => {
                    if (data.found) {
                        document.getElementById('id_rd2').value = data.rd;
                    } else {
                        document.getElementById('id_rd2').value = '';
                        alert("No se encontró el valor de RD para el VRF ingresado.");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert("Ocurrió un error al buscar el valor de RD.");
                });
        }
    });
}