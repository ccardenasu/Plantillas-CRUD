document.addEventListener('DOMContentLoaded', function() {
    var tipoServicioField = document.getElementById('id_tipo_servicio');
    var tipoEquipoField = document.getElementById('id_tipo_equipo');
    var tipoConfiguracionField = document.getElementById('id_tipo_configuracion');
    var bundleEtherField = document.getElementById('id_bundle_ether');
    var bundleEther_bField = document.getElementById('id_bundle_ether_b');
    var allFields = document.querySelectorAll('.form-control');
    var vrfField = document.getElementById('id_vrf');
    var rdField = document.getElementById('id_rd');

    var fieldsToShowVPNAMPJUN = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw', 'id_unit', 'id_bw','id_wan', 'id_bundle_ether', 'id_pe', 'id_interface_pe'];
    var fieldsToShowADIAMPJUN = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw', 'id_unit', 'id_bw','id_wan', 'id_bundle_ether', 'id_pe', 'id_interface_pe'];
    var fieldsToShowVPLSAMPJUN = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_rfs_ip_port_b', 'id_cliente', 'id_sede', 'id_sede_b', 'id_sw', 'id_interface_sw', 'id_sw_b', 'id_interface_sw_b', 'id_unit', 'id_unit_b', 'id_bw', 'id_bundle_ether', 'id_pe', 'id_interface_pe', 'id_bundle_ether_b', 'id_pe_b', 'id_interface_pe_b'];
    var fieldsToShowADIAMPALC = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw', 'id_sv', 'id_cv', 'id_bw','id_wan', 'id_bundle_ether', 'id_pe', 'id_interface_pe','id_puertos_lag'];
    var fieldsToShowVPNALTJUN = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw','id_vrf','id_rd', 'id_unit', 'id_sv', 'id_cv', 'id_bw','id_wan','id_asn','id_asn','id_lnnid', 'id_bundle_ether', 'id_pe', 'id_interface_pe'];
    var fieldsToShowADIALTALC = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw', 'id_sv', 'id_cv', 'id_bw','id_wan','id_wanv6','id_asn','lan,', 'id_bundle_ether', 'id_pe', 'id_interface_pe','id_puertos_lag'];
    var fieldsToShowVPLSMODJUN = ['id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_rfs_ip_port', 'id_rfs_ip_port_b', 'id_cliente', 'id_sede', 'id_sede_b', 'id_sw', 'id_interface_sw', 'id_sw_b', 'id_interface_sw_b', 'id_unit', 'id_unit_b', 'id_bundle_ether', 'id_pe', 'id_interface_pe', 'id_bundle_ether_b', 'id_pe_b', 'id_interface_pe_b'];

      // Agregar evento blur para vrfField
    vrfField.addEventListener('blur', function() {
        var vrfValue = vrfField.value;
        console.log('El campo VRF ha perdido el foco');
        if (vrfValue) {
            fetch(`/buscar_vrf_rd/?vrf=${vrfValue}`)
                .then(response => response.json())
                .then(data => {
                    if (data.found) {
                        rdField.value = data.rd;
                    } else {
                        rdField.value = '';
                        alert("No se encontró el valor de RD para el VRF ingresado.");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert("Ocurrió un error al buscar el valor de RD.");
                });
        }
    });


    function updateFieldVisibility() {
        var tipoConfiguracion = tipoConfiguracionField.value;
        var tipoServicio = tipoServicioField.value;
        var tipoEquipo = tipoEquipoField.value;

        

        allFields.forEach(field => {
            if (tipoConfiguracion === 'Ampliacion' && tipoServicio === "VPN" && tipoEquipo === "JUNIPER") {
                field.style.display = fieldsToShowVPNAMPJUN.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Ampliacion' && tipoServicio === "ADI" && tipoEquipo === "JUNIPER") {
                field.style.display = fieldsToShowADIAMPJUN.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Ampliacion' && tipoServicio === "VPLS" && tipoEquipo === "JUNIPER") {
                field.style.display = fieldsToShowVPLSAMPJUN.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Ampliacion' && tipoServicio === "ADI" && tipoEquipo === "ALCATEL") {
                field.style.display = fieldsToShowADIAMPALC.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Alta' && tipoServicio === "VPN" && tipoEquipo === "JUNIPER") {
                field.style.display = fieldsToShowVPNALTJUN.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Alta' && tipoServicio === "ADI" && tipoEquipo === "ALCATEL") {
                field.style.display = fieldsToShowADIALTALC.includes(field.id) ? 'block' : 'none';
            } else if (tipoConfiguracion === 'Modificacion' && tipoServicio === "VPLS"&& tipoEquipo === "JUNIPER") {
                field.style.display = fieldsToShowVPLSMODJUN.includes(field.id) ? 'block' : 'none';
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

    // Event listeners for changes
    tipoServicioField.addEventListener('change', updateFieldVisibility);
    tipoEquipoField.addEventListener('change', updateFieldVisibility);
    tipoConfiguracionField.addEventListener('change', updateFieldVisibility);
    tipoServicioField.addEventListener('change', updateBundleOptions);
    tipoConfiguracionField.addEventListener('change', updateBundleOptions);

    // Event listeners for blur
    tipoServicioField.addEventListener('blur', updateFieldVisibility);
    tipoEquipoField.addEventListener('blur', updateFieldVisibility);
    tipoConfiguracionField.addEventListener('blur', updateFieldVisibility);

    // Initial call to set visibility and bundle options
    updateFieldVisibility();
    updateBundleOptions();
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
                document.querySelector('[name="puertos_lag"]').value = data.value3;
                puertos_lag = data.value3; // Asignar el valor de la columna 8 a la variable global
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


function buscarEnCSV_b() {
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
                console.log("PE_B:", data.value2);
                console.log("Interface PE_B:", data.value2);
                resultDiv.innerHTML = `<p><strong>PE_B:</strong><br> ${data.value2}<br><br><strong>Interface PE_B:</strong><br> ${data.value1}</p>`;
                document.querySelector('[name="pe_b"]').value = data.value2;
                document.querySelector('[name="interface_pe_b"]').value = data.value1;
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

function concatenar() {
    var tipo_servicio = document.querySelector('[name="tipo_servicio"]').value;
    var sw = document.querySelector('[name="sw"]').value;
    var bundle_ether = document.querySelector('[name="bundle_ether"]').value;
    var rs_sw_be = `${tipo_servicio}${sw}${bundle_ether}`;
    document.getElementById('rs-sw-be').value = rs_sw_be;
    document.getElementById('search-term').value = rs_sw_be;
    buscarEnCSV();  // Llamar a la función buscarEnCSV
}
function concatenar_b() {
    var tipo_servicio = document.querySelector('[name="tipo_servicio"]').value;
    var sw_b = document.querySelector('[name="sw_b"]').value;
    var bundle_ether_b = document.querySelector('[name="bundle_ether_b"]').value;

    console.log("tipo_servicio:", tipo_servicio);
    console.log("sw_b:", sw_b);
    console.log("bundle_ether_b:", bundle_ether_b);

    if (!tipo_servicio || !sw_b || !bundle_ether_b) {
        console.error("Uno o más campos están vacíos o no se encontraron.");
        alert("Uno o más campos están vacíos o no se encontraron.");
        return;
    }

    var rs_sw_be_b = `${tipo_servicio}${sw_b}${bundle_ether_b}`;
    document.getElementById('rs-sw-be_b').value = rs_sw_be_b;
    document.getElementById('search-term').value = rs_sw_be_b;

    buscarEnCSV_b();
}

