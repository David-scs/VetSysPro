// JavaScript para manejar la selección de opciones (No borrar)
/* const opcionesMascota = document.querySelectorAll('.nav__a');

opcionesMascota.forEach(opcion => {
    opcion.addEventListener('click', () => {
        console.log('Clic en opción');
        // Eliminar la clase 'selected' de todas las opciones
        opcionesMascota.forEach(opcion => {
            opcion.classList.remove('selected');
        });

        // Agregar la clase 'selected' a la opción seleccionada
        opcion.classList.add('selected');
    });
});*/



        // Obtener todos los botones
        var botones = document.querySelectorAll(".boton");
        
        // Agregar el evento 'click' a cada botón
        botones.forEach(function(boton) {
          boton.addEventListener("click", function() {
            // Iterar sobre cada botón y remover la clase 'selected'
            botones.forEach(function(boton) {
              boton.classList.remove("selected");
            });
            // Agregar la clase 'selected' solo al botón actual
            this.classList.add("selected");
          });
        });
    
