import { updateFieldVisibility, updateBundleOptions } from './fieldsToShow.js';
import { concatenar_tipo_servicio_sw } from './functions.js';

export function initializeEventListeners() {
    var tipoServicioField = document.getElementById('id_tipo_servicio');
    var tipoEquipoField = document.getElementById('id_tipo_equipo');
    var tipoConfiguracionField = document.getElementById('id_tipo_configuracion');
    var swField = document.getElementById('id_sw');

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
}