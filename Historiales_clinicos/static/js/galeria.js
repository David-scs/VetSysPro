
/*Cosido para la galeria */
const fulImgBox = document.getElementById("fulImgBox")
fulImg = document.getElementById("fulIimg")

function openImg(references){
    fulImgBox.style.display = "flex"
    fulImg.src = references
}

function closeImg(){
    fulImgBox.style.display = "none";
}

/*codigo para el boton de subir archivo*/
document.getElementById("file-upload-button").addEventListener("click", function() {
    document.getElementById("file-input").click();
});

document.getElementById("file-input").addEventListener("change", function() {
    console.log("Archivo seleccionado:", this.files[0]);
});
