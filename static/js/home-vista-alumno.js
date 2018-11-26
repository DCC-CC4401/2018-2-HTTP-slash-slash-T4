{
     const body=document.getElementById('body-tabla-coev');
     const filas=body.querySelectorAll('tr');

     for(let i=0; i<filas.length; i++){
         const fila=filas[i];
         const id=fila.getAttribute('data-id-coev')
         fila.addEventListener('click', ()=>{
             location.href='/coevaluacion/' + id;
         });
     }

}