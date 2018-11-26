{	
	// Agregamos event listeners a las filas de los cursos
	// para que al ser clickeadas muestren las notas correspondientes
	const filasCursos= document.querySelectorAll('.row-curso');
	filasCursos.forEach((fila, indice, lista)=>{
		fila.addEventListener('click', (event)=>{
			const id= fila.getAttribute('data-curso-id');
			const codigo= fila.querySelector('.curso-codigo').textContent;
			const semestre= fila.querySelector('.curso-semestre').textContent;
			showNotas(id, codigo, semestre);
			event.currentTarget.classList.add('active');	
		});
	})
}

{	

	function cambiarClave(event){
		event.preventDefault();
		const form = document.getElementById('form-cambiar-clave');
		const nueva = form['clave-nueva'].value;
		const conf = form['clave-nueva-conf'].value;
		const alert = document.getElementById('alert-clave');
		if(nueva !== conf){
			alert.textContent= 'Las contraseñas nuevas no coinciden';
			alert.classList.add('alert-danger');
			return;
		}
		const datos= new FormData(form);

		fetch('/cambiar_clave', {
			method: "POST",
	        credentials: "same-origin",
	        body: datos
		}).then(response => response.json()).then(res => {
			if(res.ok==true){
				alert.textContent= 'Contraseña modificada con éxito';
				alert.classList.remove('alert-danger');
				alert.classList.add('alert-success');
				alert.style.display= "block";
				form.reset();
			}else{
				alert.textContent= 'Contraseña antigua incorrecta';
				alert.classList.remove('alert-success');
				alert.classList.add('alert-danger');
				alert.style.display= "block";
			}
		});

	}

	document.getElementById('form-cambiar-clave').addEventListener('submit', cambiarClave);
}