export function buscarCfs() {
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
export function buscarEnCSV() {
    var searchTerm = document.getElementById('search-term').value;
    if (!searchTerm) {
        alert("Por favor, ingresa un término de búsqueda.");
        return;
    }
    console.log('Buscando en CSV con término:', searchTerm);  // Verifica el término de búsqueda

    fetch(`/buscar_en_csv/?term=${searchTerm}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Respuesta del servidor:', data);  // Verifica la respuesta del servidor
            var resultDiv = document.getElementById('search-result');
            resultDiv.innerHTML = '';
            if (data.found) {
                resultDiv.innerHTML = `<strong>PE:</strong><br> ${data.value2}<br><br><strong>Interface PE:</strong><br> ${data.value1}<br><br>
                <strong>PE_VPLS_A:</strong><br> ${data.value4}<br><br><strong>INTERFACE_PE_VPLS_A:</strong><br> ${data.value5}<br><br>
                <strong>PE_VPLS_B:</strong><br> ${data.value6}<br><br><strong>INTERFACE_PE_VPLS_B:</strong><br> ${data.value7}<br><br></p>`;
                document.querySelector('[name="pe"]').value = data.value2;
                document.querySelector('[name="interface_pe"]').value = data.value1;
                

            } else {
                resultDiv.innerText = "No se encontraron resultados en el CSV.";
            }
        })
        .catch(error => {
    console.error('Error:', error);
    var resultDiv = document.getElementById('search-result');
    resultDiv.innerText = `Ocurrió un error al buscar en el CSV: ${error.message}`;
});
}

export function buscarEnCSV_b() {
    var searchTerm = document.getElementById('search-term').value;
    if (!searchTerm) {
        alert("Por favor, ingresa un término de búsqueda.");
        return;
    }
    console.log('Buscando en CSV_B con término:', searchTerm);  // Verifica el término de búsqueda

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

export function concatenar() {
    var tipo_servicio = document.querySelector('[name="tipo_servicio"]').value;
    var sw = document.querySelector('[name="sw"]').value;
    var bundle_ether = document.querySelector('[name="bundle_ether"]').value;
    var rs_sw_be = `${tipo_servicio}${sw}${bundle_ether}`;
    console.log('tipo_servicio:', tipo_servicio);
    console.log('sw:', sw);
    console.log('bundle_ether:', bundle_ether);
    document.getElementById('rs-sw-be').value = rs_sw_be;
    document.getElementById('search-term').value = rs_sw_be;
    buscarEnCSV();  // Llamar a la función buscarEnCSV
}

export function concatenar_b() {
    var tipo_servicio = document.querySelector('[name="tipo_servicio"]').value;
    var sw_b = document.querySelector('[name="sw_b"]').value;
    var bundle_ether_b = document.querySelector('[name="bundle_ether_b"]').value;

    console.log('tipo_servicio:', tipo_servicio);
    console.log('sw_b:', sw_b);
    console.log('bundle_ether_b:', bundle_ether_b);

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

export function concatenar_tipo_servicio_sw() {
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

export function fillForm(record) {
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


export function limpiarCampos() {
    var fields = document.querySelectorAll('.form-control');
    fields.forEach(field => field.value = '');
    document.getElementById('error-message').innerText = '';
    document.getElementById('record-selection').style.display = 'none';
}

export function validateForm(event) {
    console.log("validateForm ejecutado");
    var cfs = document.querySelector('[name="cfs"]').value;
    if (cfs === "") {
        document.getElementById('error-message').innerText = "El cfs es obligatorio.";
        event.preventDefault();
        window.scrollTo(0, 0);
        return false;
    }
    return true;
}
