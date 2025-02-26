import { initializeEventListeners } from './events.js';
import { updateFieldVisibility, updateBundleOptions } from './fieldsToShow.js';
import { buscarCfs, buscarEnCSV, buscarEnCSV_b, concatenar, concatenar_b, concatenar_tipo_servicio_sw, fillForm, validateForm } from './functions.js';

document.addEventListener('DOMContentLoaded', function() {
    console.log("La consola está funcionando correctamente");

    initializeEventListeners();
    console.log("Event listeners initialized");

    updateFieldVisibility();
    console.log("Field visibility updated");

    updateBundleOptions();
    console.log("Bundle options updated");

    // Asignar funciones al objeto window para que estén disponibles globalmente
    window.buscarCfs = buscarCfs;
    window.buscarEnCSV = buscarEnCSV;
    window.buscarEnCSV_b = buscarEnCSV_b;
    window.concatenar = concatenar;
    window.concatenar_b = concatenar_b;
    window.concatenar_tipo_servicio_sw = concatenar_tipo_servicio_sw;
    window.fillForm = fillForm;
    window.validateForm = validateForm;

    console.log("Functions assigned to window object");
});