// JavaScript para la búsqueda en la tabla
const searchInput = document.querySelector('.table__header .input_group input');
const tableRows = document.querySelectorAll('.table__body tbody tr');

searchInput.addEventListener('input', searchTable);

function searchTable() {
    const searchValue = searchInput.value.trim().toLowerCase();

    tableRows.forEach((row, i) => {
        const rowData = row.textContent.toLowerCase();
        row.classList.toggle('hide', rowData.indexOf(searchValue) === -1);
        row.style.setProperty('--delay', i / 25 + 's');
    });

    // Aplicar estilos a las filas visibles
    document.querySelectorAll('.table__body tbody tr:not(.hide)').forEach((visibleRow, i) => {
        visibleRow.style.backgroundColor = i % 2 === 0 ? 'transparent' : 'rgba(0, 0, 0, 0.05)';
    });
}


/*Ventana modal formulario*/
const windowBackground = document.getElementById('window-background')
const windowContainer = document.getElementById('window-container')
const openButton = document.getElementById('open-button')
const closeButton = document.getElementById('close-button')


openButton.addEventListener('click', ()=>windowBackground.style.display='flex')

const closeWindow = ()=>{
    windowContainer.classList.add('close')
    setTimeout(() =>{
        windowContainer.classList.remove('close')
        windowBackground.style.display='none'
    }, 1000);   
}

closeButton.addEventListener('click', ()=>closeWindow())


// Función para mostrar la ventana modal confirmacion
function confirmarEnvio() {
    var modal = document.getElementById("modal");
    modal.style.display = "block";
    return false; 
  }

// Función para enviar el formulario desde la ventana de confirmacion
function enviarFormulario() {
    document.getElementById("formularioMascota").submit();
    
}

// Función para cerrar la ventana modal de confirmacion
function cerrarModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
  }