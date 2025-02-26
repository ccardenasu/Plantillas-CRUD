import { initializeEventListeners } from './eventHandlers.js';
import { updateFieldVisibility, updateBundleOptions } from './fieldsToShow.js';

document.addEventListener('DOMContentLoaded', function() {
    console.log("La consola está funcionando correctamente");

    initializeEventListeners();
    updateFieldVisibility();
    updateBundleOptions();
});