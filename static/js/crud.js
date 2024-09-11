// static/js/crud.js
console.log("Archivo crud.js cargado correctamente");

document.addEventListener('DOMContentLoaded', function() {
    var tipoServicioField = document.getElementById('id_tipo_servicio');
    var tipoEquipoField = document.getElementById('id_tipo_equipo');
    var tipoConfiguracionField = document.getElementById('id_tipo_configuracion');
    var bundleEtherField = document.getElementById('id_bundle_ether');
    var bundleEther_bField = document.getElementById('id_bundle_ether_b');
    var allFields = document.querySelectorAll('.form-control');

    var fieldsToShowVPN = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw', 'id_unit', 'id_bw','id_wan', 'id_bundle_ether', 'id_pe', 'id_interface_pe'];
    var fieldsToShowVPLS = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_rfs_ip_port', 'id_rfs_ip_port_b', 'id_cliente', 'id_sede', 'id_sede_b', 'id_sw', 'id_interface_sw', 'id_sw_b', 'id_interface_sw_b', 'id_unit', 'id_unit_b', 'id_bw', 'id_bundle_ether', 'id_pe', 'id_interface_pe', 'id_bundle_ether_b', 'id_pe_b', 'id_interface_pe_b'];
    var fieldsToShowModificacionVPLS = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_rfs_ip_port', 'id_rfs_ip_port_b', 'id_cliente', 'id_sede', 'id_sede_b', 'id_sw', 'id_interface_sw', 'id_sw_b', 'id_interface_sw_b', 'id_unit', 'id_unit_b', 'id_bundle_ether', 'id_pe', 'id_interface_pe', 'id_bundle_ether_b', 'id_pe_b', 'id_interface_pe_b'];
    var fieldsToShowADIAMPALCATEL = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw', 'id_unit', 'id_bw','id_wan', 'id_bundle_ether', 'id_pe', 'id_interface_pe'];

    function updateFieldVisibility() {
        var tipoConfiguracion = tipoConfiguracionField.value;
        var tipoServicio = tipoServicioField.value;
        var tipoEquipo = tipoEquipoField.value;

        allFields.forEach(field => {
            if (tipoConfiguracion === 'Ampliacion' && tipoServicio === "VPN") {
                field.style.display = fieldsToShowVPN.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Ampliacion' && tipoServicio === "VPLS") {
                field.style.display = fieldsToShowVPLS.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Modificacion' && tipoServicio === "VPLS") {
                field.style.display = fieldsToShowModificacionVPLS.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Ampliacion' && tipoServicio === "ADI" && tipoEquipo === "ALCATEL") {
                field.style.display = fieldsToShowADIAMPALCATEL.includes(field.id) ? 'block' : 'none';
            } else {
                field.style.display = 'block';
            }
        });
    }

    function updateBundleOptions() {
        var optionsVPNVPLS = `
            <option value="N/A">N/A</option>
            <option value="Bundle-ether10">Bundle-ether10</option>
            <option value="Bundle-ether11">Bundle-ether11</option>
            <option value="Bundle-ether14">Bundle-ether14</option>
        `;
        var optionsDefault = `
            <option value="N/A">N/A</option>
            <option value="">Seleccione una opción</option>
            <option value="Bundle-ether12">Bundle-ether12</option>
            <option value="Bundle-ether13">Bundle-ether13</option>
            <option value="Bundle-ether32">Bundle-ether32</option>
            <option value="Bundle-ether33">Bundle-ether33</option>
        `;

        var options = (tipoServicioField.value === 'VPN' || tipoServicioField.value === 'VPLS') ? optionsVPNVPLS : optionsDefault;
        bundleEtherField.innerHTML = options;
        bundleEther_bField.innerHTML = options;
    }

    tipoConfiguracionField.addEventListener('change', updateFieldVisibility);
    tipoServicioField.addEventListener('change', updateFieldVisibility);
    tipoServicioField.addEventListener('change', updateBundleOptions);

    updateFieldVisibility(); // Set initial state
    updateBundleOptions(); // Set initial bundle options
});

function buscarCfs() {
    var cfs = document.getElementById('id_cfs').value;
    console.log(`Buscando CFS: ${cfs}`);
    fetch(`/buscar_cfs/?cfs=${cfs}`)
        .then(response => response.json())
        .then(data => {
            console.log('Datos recibidos:', data);
            var errorMessage = document.getElementById('error-message');
            if (data.exists) {
                errorMessage.innerText = "";
                if (data.records.length > 1) {
                    var select = document.getElementById('record-select');
                    select.innerHTML = '';
                    data.records.forEach(record => {
                        var option = document.createElement('option');
                        option.value = JSON.stringify(record);
                        option.text = `Registro ${record.id} - ${record.created_at}`;
                        select.appendChild(option);
                    });
                    document.getElementById('record-selection').style.display = 'block';
                } else {
                    fillForm(JSON.stringify(data.records[0]));
                }
            } else {
                errorMessage.innerText = "El CFS no existe.";
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function fillForm(record) {
    var data = JSON.parse(record);
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            var field = document.querySelector(`[name="${key}"]`);
            if (field) {
                field.value = data[key];
            }
        }
    }
}

function limpiarCampos() {
    var fields = document.querySelectorAll('.form-control');
    fields.forEach(field => field.value = '');
    document.getElementById('error-message').innerText = '';
    document.getElementById('record-selection').style.display = 'none';
}

function validateForm(event) {
    var nombre = document.querySelector('[name="nombre"]').value;
    if (nombre === "") {
        document.getElementById('error-message').innerText = "El nombre es obligatorio.";
        event.preventDefault();
        window.scrollTo(0, 0);
        return false;
    }
    return true;
}

function buscarEnCSV() {
    var searchTerm = document.getElementById('search-term').value;
    if (!searchTerm) {
        alert("Por favor, ingresa un término de búsqueda.");
        return;
    }
    fetch(`/buscar_en_csv/?term=${searchTerm}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            var resultDiv = document.getElementById('search-result');
            resultDiv.innerHTML = '';
            if (data.found) {
                resultDiv.innerHTML = `<p><strong>PE:</strong><br> ${data.value2}<br><br><strong>Interface PE:</strong><br> ${data.value1}</p>`;
                document.querySelector('[name="pe"]').value = data.value2;
                document.querySelector('[name="interface_pe"]').value = data.value1;
                 puertos_lag = data.value7; // Asignar el valor de la columna 7 a la variable global
            } else {
                resultDiv.innerText = "No se encontraron resultados en el CSV.";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            var resultDiv = document.getElementById('search-result');
            resultDiv.innerText = "Ocurrió un error al buscar en el CSV.";
        });
}

