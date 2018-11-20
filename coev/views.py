from django.shortcuts import render , redirect
from .models import Curso
from .models import Equipo
from .models import Integrante_Equipo
from .models import Admin
from .models import Coevaluacion
from .models import Info_Coevaluacion
from .models import Integrante_Curso
from .forms import LoginForm

from .forms import CrearCurso   
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            #TODO: logear al usuario con django
            return HttpResponseRedirect('/home/alumnos')
    return render(request, "coev/login.html", {'form': LoginForm()})

def homeVistaAlum(request):
    return render(request, "coev/home-vista-alumno.html")


def homeVistaDoc(request):

    if request.method == 'POST':
        if request.POST['agregar']=='Curso':
            form=CrearCurso(request.POST)
            if form.is_valid():
                curso_nombre=form.cleaned_data['codigo']
                curso_seccion=form.cleaned_data['seccion']
                curso_año=form.cleaned_data['año']
                curso_semestre=form.cleaned_data['semestre']
                nuevo_curso=Curso(nombre='PH',seccion=curso_seccion, año=curso_año,semestre=curso_semestre,codigo=curso_nombre)
                nuevo_curso.save()

    
    coevaluaciones = Coevaluacion.objects.order_by('fecha_inicio')

    cursos = Curso.objects.order_by('año')
    formCurso = CrearCurso()

    return render(request, "coev/home-vista-profesor.html", {'coev': coevaluaciones,
                                                             'cursos': cursos,
                                                             'formCurso':formCurso})



def cursoVistaDoc(request):

    return render(request, "coev/curso-vista-docente.html")

def cursoVistaAlm(request):

    return render(request, "coev/curso-vista-alumno.html")

def coevDoc(request):

    return render(request,"coev/coevaluacion-vista-docente.html")

def coevAlm(request):

    return render(request, "coev/coevaluacion-vista-alumno.html")

def perfilVistaDueno(request):

    return render(request,"coev/perfil-vista-dueno.html")

def perfilVistaDoc(request):

    return render(request,"coev/perfil-alumno-vista-docente.html")