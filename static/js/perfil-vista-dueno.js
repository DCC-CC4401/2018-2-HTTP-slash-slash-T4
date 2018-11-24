{
	const filasCursos= document.querySelectorAll('.row-curso');
	filasCursos.forEach((fila, indice, lista)=>{
		fila.addEventListener('click', (event)=>{
			const id= fila.getAttribute('data-curso-id');
			const codigo= fila.querySelector(".curso-codigo").textContent;
			const semestre= fila.querySelector(".curso-semestre").textContent;
			showNotas(id, codigo, semestre);
			event.currentTarget.classList.add('active');	
		});
	})
}