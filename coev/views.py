from django.shortcuts import render , redirect
from .models import Curso
from .models import Equipo
from .models import Integrante_Equipo
from .models import Admin
from .models import Coevaluacion
from .models import Info_Coevaluacion
from .models import Integrante_Curso
from .forms import LoginForm
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            usuario= authenticate(username= form.cleaned_data['rut'],
                                password= form.cleaned_data['clave'])
            if usuario is not None:
                if usuario.is_superuser:
                    return redirect('/admin/')
                return redirect('/home/alumnos')

        return render(request, "coev/login.html", {'form': LoginForm(), 'error': True})
                
    else:
        return render(request, "coev/login.html", {'form': LoginForm(), 'error': False})

def homeVistaAlum(request):
    return render(request, "coev/home-vista-alumno.html")


def homeVistaDoc(request):


    
    coevaluaciones = Coevaluacion.objects.order_by('fecha_inicio')

    cursos= Curso.objects.order_by('año')

    return render(request, "coev/home-vista-profesor.html", {'coev': coevaluaciones,
                                                             'cursos': cursos})



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