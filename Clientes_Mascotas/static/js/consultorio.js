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
    document.getElementById("formularioPropietario").submit();
    
}

// Función para cerrar la ventana modal de confirmacion
function cerrarModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
  }