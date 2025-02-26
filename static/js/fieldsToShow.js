console.log("fieldsToShow.js cargado");


export function updateFieldVisibility() {
    console.log("updateFieldVisibility ejecutado");

    var tipoConfiguracionField = document.getElementById('id_tipo_configuracion');
    var tipoServicioField = document.getElementById('id_tipo_servicio');
    var tipoEquipoField = document.getElementById('id_tipo_equipo');
    var swField = document.getElementById('id_sw');
    var allFields = document.querySelectorAll('.form-control');

    var tipoConfiguracion = tipoConfiguracionField.value;
    var tipoServicio = tipoServicioField.value;
    var tipoEquipo = tipoEquipoField.value;

    var fieldsToShowVPLSALTJUN = ['id_be', 'id_bundle_ether', 'id_bundle_ether_b', 'id_bw', 'id_cfs', 'id_cliente', 'id_cv', 'id_cv_b', 'id_dko', 'id_interface_pe', 'id_interface_pe_b', 'id_interface_sw', 'id_interface_sw_b', 'id_lnnid', 'id_pe', 'id_pe_b', 'id_rfs_ip_port', 'id_rfs_ip_port_b', 'id_sede', 'id_sede_b', 'id_sv', 'id_sv_b', 'id_sw', 'id_sw_b', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit', 'id_unit_b', 'id_vrf'];
    var fieldsToShowVPLSAMPJUN = ['id_bundle_ether', 'id_bundle_ether_b', 'id_bw', 'id_cfs', 'id_cliente', 'id_dko', 'id_interface_pe', 'id_interface_pe_b', 'id_interface_sw', 'id_interface_sw_b', 'id_pe', 'id_pe_b', 'id_rfs_ip_port', 'id_rfs_ip_port_b', 'id_sede', 'id_sede_b', 'id_sw', 'id_sw_b', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit', 'id_unit_b', 'id_wan'];
    var fieldsToShowVPLSMODJUN = ['id_bundle_ether', 'id_bundle_ether_b', 'id_cfs', 'id_cliente', 'id_dko', 'id_interface_pe', 'id_interface_pe_b', 'id_interface_sw', 'id_interface_sw_b', 'id_pe', 'id_pe_b', 'id_rfs_ip_port', 'id_rfs_ip_port_b', 'id_sede', 'id_sede_b', 'id_sw', 'id_sw_b', 'id_tipo_configuracion', 'id_tipo_servicio', 'id_unit', 'id_unit_b'];
    var fieldsToShowVPNMODJUN = ['id_bundle_ether', 'id_cfs', 'id_cliente', 'id_dko', 'id_interface_pe', 'id_interface_sw', 'id_pe', 'id_rfs_ip_port', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit'];
    var fieldsToShowVPNALTJUN = ['id_asn', 'id_be', 'id_bundle_ether', 'id_bw', 'id_bw_exchange', 'id_bw_plus', 'id_bw_voz', 'id_bw_video', 'id_cfs', 'id_cliente', 'id_cv', 'id_dko', 'id_interface_pe', 'id_interface_sw', 'id_lbcpe', 'id_lnnid', 'id_pe', 'id_puertos_lag', 'id_rd', 'id_rd2', 'id_rfs_ip_port', 'rfs-ip-port_b', 'id_sede', 'id_sv', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit', 'id_vrf', 'id_vrf_init', 'id_vrf2', 'id_vt', 'id_wan', 'id_wanv6'];
    var fieldsToShowNNIALTJUN = ['id_asn', 'id_be', 'id_bundle_ether', 'id_bw', 'id_bw_exchange', 'id_bw_plus', 'id_bw_voz', 'id_bw_video', 'id_cfs', 'id_cliente', 'id_cv', 'id_dko', 'id_interface_pe', 'id_interface_sw', 'id_lbcpe', 'id_lnnid', 'id_pe', 'id_puertos_lag', 'id_rd', 'id_rd2', 'id_rfs_ip_port', 'rfs-ip-port_b', 'id_sede', 'id_sv', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit', 'id_vrf', 'id_vrf_init', 'id_vrf2', 'id_vt', 'id_wan', 'id_wanv6'];
    var fieldsToShowVPNAMPJUN = ['id_be', 'id_bundle_ether', 'id_bw', 'id_cfs', 'id_cliente', 'id_dko', 'id_interface_pe', 'id_interface_sw', 'id_pe', 'id_rfs_ip_port', 'id_sede', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit', 'id_wan'];
    var fieldsToShowADIALTALC = ['id_asn', 'id_bundle_ether', 'id_bw', 'id_cfs', 'id_cliente', 'id_cv', 'id_dko', 'id_ies', 'id_interface_pe', 'id_interface_sw', 'id_lan', 'id_lanv6', 'id_lnnid', 'id_pe', 'id_puertos_lag', 'id_rfs_ip_port', 'id_sede', 'id_sv', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_vt', 'id_wan', 'id_wanv6'];
    var fieldsToShowADIALTALCV = ['id_asn', 'id_be', 'id_bundle_ether', 'id_bw', 'id_cfs', 'id_cliente', 'id_cv', 'id_dko', 'id_encap_type', 'id_ies', 'id_interface_pe', 'id_interface_sw', 'id_lag', 'id_lan', 'id_lanv6', 'id_lnnid', 'id_pe', 'id_puertos_lag', 'id_rfs_ip_port', 'id_sede', 'id_sv', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_vt', 'id_wan', 'id_wanv6'];
    var fieldsToShowADIALTJUN = ['id_asn', 'id_be', 'id_bundle_ether', 'id_bw', 'id_cfs', 'id_cliente', 'id_cv', 'id_dko', 'id_interface_pe', 'id_interface_sw', 'id_lan', 'id_lanv6', 'id_lnnid', 'id_pe', 'id_rfs_ip_port', 'id_rfs_ip_port_nid', 'id_sede', 'id_sv', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit', 'id_unit_nid', 'id_vt', 'id_wan', 'id_wanv6'];
    var fieldsToShowADIAMPALC = ['id_bundle_ether', 'id_bw', 'id_cfs', 'id_cliente', 'id_cv', 'id_dko', 'id_interface_pe', 'id_interface_sw', 'id_lag', 'id_pe', 'id_puertos_lag', 'id_rfs_ip_port', 'id_sede', 'id_sv', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_wan'];
    var fieldsToShowADIAMPJUN = ['id_bundle_ether', 'id_bw', 'id_cfs', 'id_cliente', 'id_dko', 'id_interface_pe', 'id_interface_sw', 'id_pe', 'id_rfs_ip_port', 'id_sede', 'id_sw', 'id_tipo_configuracion', 'id_tipo_equipo', 'id_tipo_servicio', 'id_unit', 'id_wan'];
            


    // Define your fieldsToShow arrays here or import them if they are in another module

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
        } else if (tipoConfiguracion === 'Alta' && tipoServicio === "NNI_L3_impsat" && tipoEquipo === "JUNIPER") {
            field.style.display = fieldsToShowNNIALTJUN.includes(field.id) ? 'block' : 'none';
        } else if (tipoConfiguracion === 'Alta' && tipoServicio === "ADI" && tipoEquipo === "ALCATEL") {
            field.style.display = fieldsToShowADIALTALC.includes(field.id) ? 'block' : 'none';
        } else if (tipoConfiguracion === 'Alta' && tipoServicio === "ADI" && tipoEquipo === "ALCATEL_V") {
            field.style.display = fieldsToShowADIALTALCV.includes(field.id) ? 'block' : 'none';    
        } else if (tipoConfiguracion === 'Alta' && tipoServicio === "ADI" && tipoEquipo === "JUNIPER") {
            field.style.display = fieldsToShowADIALTJUN.includes(field.id) ? 'block' : 'none';
        } else if (tipoConfiguracion === 'Alta' && tipoServicio === "VPLS" && tipoEquipo === "JUNIPER") {
            field.style.display = fieldsToShowVPLSALTJUN.includes(field.id) ? 'block' : 'none';
        } else if (tipoConfiguracion === 'Modificacion' && tipoServicio === "VPLS" && tipoEquipo === "JUNIPER") {
            field.style.display = fieldsToShowVPLSMODJUN.includes(field.id) ? 'block' : 'none';
        } else if (tipoConfiguracion === 'Modificacion' && tipoServicio === "VPN" && tipoEquipo === "JUNIPER") {
            field.style.display = fieldsToShowVPNMODJUN.includes(field.id) ? 'block' : 'none';
        } else {
            field.style.display = 'block';
        }
    });
}

export function updateBundleOptions() {
    var tipoServicioField = document.getElementById('id_tipo_servicio');
    var bundleEtherField = document.getElementById('id_bundle_ether');
    var bundleEther_bField = document.getElementById('id_bundle_ether_b');

    var optionsVPNVPLS = `
        <option value="N/A">N/A</option>
        <option value="Bundle-ether10">Bundle-ether10</option>
        <option value="Bundle-ether11">Bundle-ether11</option>
        <option value="Bundle-ether14">Bundle-ether14</option>
        <option value="TE7/3">TE7/3</option>
        <option value="ae1">ae1</option>
        <option value="ae3">ae3</option>
        <option value="Port-channel3">Port-channel3</option>
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