function jumpTo(anchor) {
	document.getElementById(anchor).scrollIntoView();
}

/* Home page */

function addCoev() {
    document.getElementById("add-coev-form").style.display = "block";
    document.getElementById("add-curso-form").style.display = "none";
    document.getElementById("add-coev-btn").classList.add("active");
    document.getElementById("add-curso-btn").classList.remove("active");
}

function addCurso() {
    document.getElementById("add-coev-form").style.display = "none";
    document.getElementById("add-curso-form").style.display = "block";
    document.getElementById("add-coev-btn").classList.remove("active");
    document.getElementById("add-curso-btn").classList.add("active");
}

function cancelAdd() {
    document.getElementById("add-coev-form").style.display = "none";
    document.getElementById("add-curso-form").style.display = "none";
    document.getElementById("add-coev-btn").classList.remove("active");
    document.getElementById("add-curso-btn").classList.remove("active");
}

/* Perfil */

function changePass() {
    document.getElementById("cambiar-contrasena").style.display = "block";
    document.getElementById("notas-resumen").style.display = "none";
    document.getElementById("notas-placeholder").style.display = "none";
    document.getElementById("change-pass-btn").classList.add("active");
    document.getElementById("row-btn").classList.remove("active");
    const alert = document.getElementById('alert-clave');
    alert.style.display= "none";
}

function showNotas(idCurso, codigo, semestre) {
    // Escondemos el formulario de claves y el texto inicial:
    document.getElementById("cambiar-contrasena").style.display = "none";
    document.getElementById("notas-placeholder").style.display = "none";
    const changePass = document.getElementById("change-pass-btn");
    if (changePass !== null) changePass.classList.remove("active");
    document.querySelectorAll(".row-curso").forEach((fila, indice, lista)=>{
        fila.classList.remove('active');
    })

    // Mostramos la tabla de notas:
    const resumen= document.getElementById("notas-resumen");
    resumen.style.display= "block";

    // Mostramos el codigo y semestre del nuevo curso:
    resumen.querySelector('#currentCurso').textContent= codigo+", "+semestre; 

    // Escondemos las notas del curso actual:
    const idActual= resumen.getAttribute("data-curso-id-actual");
    if(idActual!=""){
        const tbodyActual= document.querySelector(`tbody[data-curso-id="${idActual}"]`);
        if(tbodyActual !== null) tbodyActual.style.display= "none";
    }

    // Mostramos las notas correspondientes al id:
    const tbody= document.querySelector(`tbody[data-curso-id="${idCurso}"]`);
    if(tbody !== null){
        tbody.style.display= "table-row-group";
        resumen.setAttribute("data-curso-id-actual", idCurso);
    }
}

function cancelPass() {
    document.getElementById("cambiar-contrasena").style.display = "none";
    document.getElementById("notas-resumen").style.display = "none";
    document.getElementById("change-pass-btn").classList.add("active");
    document.getElementById("notas-placeholder").style.display = "block";
}

/* Gestión Curso */

function showGestionEstudiante() {
    document.getElementById("gestion-grupo").style.display = "none";
    document.getElementById("gestion-estudiante").style.display = "block";
    document.getElementById("gestion-placeholder").style.display = "none";
    document.getElementById("active-estudiante").classList.add("active");
    document.getElementById("active-grupo").classList.remove("active");
}

function showGestionGrupo() {
    document.getElementById("gestion-grupo").style.display = "block";
    document.getElementById("gestion-estudiante").style.display = "none";
    document.getElementById("gestion-placeholder").style.display = "none";
    document.getElementById("active-grupo").classList.add("active");
    document.getElementById("active-estudiante").classList.remove("active");
}