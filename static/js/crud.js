    document.addEventListener('DOMContentLoaded', function() {
        var tipoServicioField = document.getElementById('id_tipo_servicio');
        var tipoEquipoField = document.getElementById('id_tipo_equipo');
        var tipoConfiguracionField = document.getElementById('id_tipo_configuracion');
        var bundleEtherField = document.getElementById('id_bundle_ether');
        var bundleEther_bField = document.getElementById('id_bundle_ether_b');
        var allFields = document.querySelectorAll('.form-control');
        var vrfField = document.getElementById('id_vrf');
        var rdField = document.getElementById('id_rd');
        var swField = document.getElementById('id_sw');
        var svField = document.getElementById('id_sv');

        var fieldsToShowVPLSALTJUN = 	[ 'id_be','id_bw','id_bundle_ether','id_bundle_ether_b','id_cfs','id_cliente','id_cv','id_cv_b','id_dko','id_interface_pe','id_interface_pe_b',
            'id_interface_sw','id_interface_sw_b','id_lnnid','id_pe','id_pe_b','id_rfs_ip_port','id_rfs_ip_port_b','id_sede','id_sede_b','id_sv','id_sv_b','id_sw','id_sw_b','id_tipo_configuracion',
            'id_tipo_equipo','id_tipo_servicio','id_unit','id_unit_b','id_vrf',];
        var fieldsToShowVPLSAMPJUN =    [ 'id_bw','id_bundle_ether','id_bundle_ether_b','id_cfs','id_cliente','id_dko','id_interface_pe','id_interface_pe_b','id_interface_sw','id_interface_sw_b',
            'id_pe','id_pe_b','id_rfs_ip_port','id_rfs_ip_port_b','id_sede','id_sede_b','id_sw','id_sw_b','id_tipo_configuracion','id_tipo_equipo','id_tipo_servicio','id_unit','id_unit_b','id_wan'];    
        var fieldsToShowVPLSMODJUN = 	[ 'id_bundle_ether','id_bundle_ether_b','id_cfs','id_cliente','id_dko','id_interface_pe','id_interface_pe_b','id_interface_sw','id_interface_sw_b','id_pe',
            'id_pe_b','id_rfs_ip_port','id_rfs_ip_port_b','id_sede','id_sede_b','id_sw','id_sw_b','id_tipo_configuracion','id_tipo_servicio','id_unit','id_unit_b'];
        var fieldsToShowVPNMODJUN = 	[ 'id_bundle_ether','id_cfs','id_cliente','id_dko','id_interface_pe','id_interface_sw','id_pe','id_rfs_ip_port','id_sw','id_tipo_configuracion',
            'id_tipo_equipo','id_tipo_servicio','id_unit',];
        var fieldsToShowVPNALTJUN =     [ 'id_asn','id_be','id_bw','id_bw_plus','id_bw_Exchange','id_bundle_ether','id_cfs','id_cliente','id_cv','id_dko','id_interface_pe','id_interface_sw',
            'id_lbcpe','id_lnnid','id_pe','id_rd','id_rfs_ip_port','id_sede','id_sv','id_sw','id_tipo_configuracion','id_tipo_equipo','id_tipo_servicio','id_unit','id_vrf','id_vt','id_wan',
            'id_wanv6','id_puertos_lag'];      
        var fieldsToShowVPNAMPJUN =     [ 'id_bw','id_bundle_ether','id_cfs','id_cliente','id_dko','id_interface_pe','id_interface_sw','id_pe','id_rfs_ip_port','id_sede','id_sw',
            'id_tipo_configuracion','id_tipo_equipo','id_tipo_servicio','id_unit','id_wan'];
        var fieldsToShowADIALTALC =     [ 'id_asn','id_cfs', 'id_dko', 'id_IES', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 
            'id_interface_sw', 'id_vt', 'id_sv', 'id_cv', 'id_bw','id_wan','id_wanv6','id_lan','id_lanv6','id_lnnid', 'id_bundle_ether', 'id_pe', 'id_interface_pe','id_puertos_lag'];
        var fieldsToShowADIALTALCV =     [ 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_dko','id_cfs','id_cliente', 'id_sede','id_rfs_ip_port','id_vt','id_sw','id_interface_sw',
             'id_bw','id_sv', 'id_cv','id_IES','id_lag','id_puertos_lag','id_asn','id_wan','id_wanv6','id_lan','id_lanv6','id_be','id_bundle_ether', 'id_pe', 'id_interface_pe','id_encap_type',];
        var fieldsToShowADIALTJUN =     [ 'id_asn','id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_vt','id_sw', 
            'id_interface_sw', 'id_unit', 'id_sv', 'id_cv', 'id_bw','id_wan','id_wanv6','id_lan','id_lanv6','id_lnnid','id_be','id_bundle_ether', 'id_pe', 'id_interface_pe'];
        var fieldsToShowADIAMPALC =     [ 'id_cfs', 'id_dko', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_tipo_equipo', 'id_rfs_ip_port', 'id_cliente', 'id_sede', 'id_sw', 'id_interface_sw', 
            'id_sv', 'id_cv', 'id_bw','id_wan', 'id_bundle_ether', 'id_pe', 'id_interface_pe','id_puertos_lag','id_lag'];
        var fieldsToShowADIAMPJUN =     [ 'id_bw','id_bundle_ether','id_cfs','id_cliente','id_dko','id_interface_pe','id_interface_sw','id_pe','id_rfs_ip_port','id_sede','id_sw',
            'id_tipo_configuracion','id_tipo_equipo','id_tipo_servicio','id_unit','id_wan'];
        // Agregar evento blur para vrfField

        
        swField.addEventListener('blur', function() {
            console.log("Evento blur activado");
            console.log("Valor de swField:", swField.value);
            
            if (swField.value === "mesc20.baq.baq") {
                console.log("Valor encontrado: mesc20.baq.baq");
                svField.value = "1900";
            } else if (swField.value === "mesb10.morato.telefonica.bog") {
                console.log("Valor encontrado: mesb10.morato.telefonica.bog");
                svField.value = "19xx, ADI 2411";            
            } else {
                console.log("Valor no encontrado");
            }
        });
        
        
        

        vrfField.addEventListener('blur', function() {
            var vrfValue = vrfField.value;
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
            var sw = swField.value;

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
                } else if (tipoConfiguracion === 'Alta' && tipoServicio === "ADI" && tipoEquipo === "ALCATEL_V") {
                    field.style.display = fieldsToShowADIALTALCV.includes(field.id) ? 'block' : 'none';    
                } else if (tipoConfiguracion === 'Alta' && tipoServicio === "ADI" && tipoEquipo === "JUNIPER") {
                    field.style.display = fieldsToShowADIALTJUN .includes(field.id) ? 'block' : 'none';
                } else if (tipoConfiguracion === 'Alta' && tipoServicio === "VPLS" && tipoEquipo === "JUNIPER") {
                    field.style.display = fieldsToShowVPLSALTJUN.includes(field.id) ? 'block' : 'none';
                } else if (tipoConfiguracion === 'Modificacion' && tipoServicio === "VPLS"&& tipoEquipo === "JUNIPER") {
                    field.style.display = fieldsToShowVPLSMODJUN.includes(field.id) ? 'block' : 'none';
                } else if (tipoConfiguracion === 'Modificacion' && tipoServicio === "VPN"&& tipoEquipo === "JUNIPER") {
                    field.style.display = fieldsToShowVPNMODJUN.includes(field.id) ? 'block' : 'none';
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
                <option value="TE7/3">TE7/3</option>
                <option value="ae1">ae1</option>

            `;
            var optionsDefault = `
                <option value="N/A">N/A</option>
                <option value="">Seleccione una opción</option>
                <option value="Bundle-ether12">Bundle-ether12</option>
                <option value="Bundle-ether13">Bundle-ether13</option>
                <option value="Bundle-ether32">Bundle-ether32</option>
                <option value="Bundle-ether33">Bundle-ether33</option>
                <option value="SUBA">SUBA</option>
                <option value="CXV">CXV</option>
                <option value="ae1">ae1</option>
                <option value="ae2">ae2</option>

            `;

            var options = (tipoServicioField.value === 'VPN' || tipoServicioField.value === 'VPLS') ? optionsVPNVPLS : optionsDefault;
            bundleEtherField.innerHTML = options;
            bundleEther_bField.innerHTML = options;
        }

        // Event listeners for changes
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
        } else {
        }
        
        updateFieldVisibility();
        updateBundleOptions();
    });

    function buscarCfs() {
        var cfs = document.getElementById('id_cfs').value;
        console.log('CFS:', cfs);  // Verifica el valor de CFS
    
        fetch(`/buscar_cfs/?cfs=${cfs}`)
            .then(response => response.json())
            .then(data => {
                console.log('Data:', data);  // Verifica la respuesta del servidor
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
                    errorMessage.style.color = 'red';  // Opcional: Cambia el color del mensaje de error
                }
            })
            .catch(error => {
                console.error('Error:', error);
                var errorMessage = document.getElementById('error-message');
                errorMessage.innerText = "Ocurrió un error al buscar el CFS.";
                errorMessage.style.color = 'red';  // Opcional: Cambia el color del mensaje de error
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
                    resultDiv.innerHTML = `<strong>PE:</strong><br> ${data.value2}<br><br><strong>Interface PE:</strong><br> ${data.value1}<br><br>
                    <strong>PE_VPLS_A:</strong><br> ${data.value4}<br><br><strong>INTERFACE_PE_VPLS_A:</strong><br> ${data.value5}<br><br>
                    <strong>PE_VPLS_B:</strong><br> ${data.value6}<br><br><strong>INTERFACE_PE_VPLS_B:</strong><br> ${data.value7}<br><br></p>`;
                    document.querySelector('[name="pe"]').value = data.value2;
                    document.querySelector('[name="interface_pe"]').value = data.value1;
                    document.querySelector('[name="puertos_lag"]').value = data.value3;
                    document.querySelector('[name="pe_vpls_a"]').value = data.value4;
                    document.querySelector('[name="interface_pe_vpls_a"]').value = data.value5;
                    document.querySelector('[name="pe_vpls_b"]').value = data.value6;
                    document.querySelector('[name="interface_pe_vpls_b"]').value = data.value7;
                    document.querySelector('[name="lb_pe_vpls_a"]').value = data.value8;
                    document.querySelector('[name="lb_pe_vpls_b"]').value = data.value9;
                    
                    puertos_lag = data.value3;
                    pe_vpls_a = data.value4;
                    interface_pe_vpls_a = data.value5;
                    pe_vpls_b = data.value6;
                    interface_pe_vpls_b = data.value7;
                    lb_pe_vpls_a = data.value8;
                    lb_pe_vpls_b = data.value9;

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

    function concatenar_tipo_servicio_sw() {
        var tipo_servicio = document.querySelector('[name="tipo_servicio"]').value;
        var sw = document.querySelector('[name="sw"]').value;
        var rs_tipo_servicio_sw = `${tipo_servicio}${sw}`;
        document.getElementById('rs-tipo-servicio-sw').value = rs_tipo_servicio_sw;
        document.getElementById('search-term').value = rs_tipo_servicio_sw;
    
        fetch(`/buscar_en_csv_tipo_servicio_sw/?term=${rs_tipo_servicio_sw}`)
            .then(response => response.json())
            .then(data => {
                var errorMessage = document.getElementById('error-message');
                if (data.found) {
                    errorMessage.innerText = "";
                    document.querySelector('[name="be"]').value = data.value5; // Asignar el valor de la columna 5
    
                    // Actualizar los campos bundle_ether y bundle_ether_b
                    var bundleEtherField = document.getElementById('id_bundle_ether');
                    var options = `<option value="${data.bundle_ether}">${data.bundle_ether}</option>`;
                    bundleEtherField.innerHTML = options;
                } else {
                    errorMessage.innerText = "No se encontraron resultados en el CSV.";
                }
            })
            .catch(error => {
                console.error('Error:', error);
                var errorMessage = document.getElementById('error-message');
                errorMessage.innerText = "Ocurrió un error al buscar en el CSV.";
            });
    }
    