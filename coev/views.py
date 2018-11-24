from django.shortcuts import render , redirect
from .models import Curso
from .models import Equipo
from .models import Integrante_Equipo
from .models import Admin
from .models import Coevaluacion
from .models import Info_Coevaluacion
from .models import Integrante_Curso
from .forms import LoginForm
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            #TODO: logear al usuario con django
            return HttpResponseRedirect('/curso/2018/Primavera/CC4401/1')
    return render(request, "coev/login.html", {'form': LoginForm()})

def homeVistaAlum(request):
    return render(request, "coev/home-vista-alumno.html")


def homeVistaDoc(request):


    
    coevaluaciones = Coevaluacion.objects.order_by('fecha_inicio')

    cursos= Curso.objects.order_by('año')

    return render(request, "coev/home-vista-profesor.html", {'coev': coevaluaciones,
                                                             'cursos': cursos})



def cursoVistaDoc(request):

    return render(request, "coev/curso-vista-docente.html")

def cursoVistaAlm(request,year,semestre,codigo,seccion):

    curso=Curso.objects.get(codigo=codigo,año=year, semestre=semestre,seccion=seccion)
    coevs=Coevaluacion.objects.filter(curso_id=curso.id).filter(info_coevaluacion__respondida=False)
    #.filter(info_coevaluacion__rut_usuario=request.user)
    Resto=Coevaluacion.objects.filter(curso_id=curso.id).exclude(info_coevaluacion__respondida=False)

    return render(request, "coev/curso-vista-alumno.html",{'curso' : curso,'coevs':coevs,'resto':Resto})

def coevDoc(request):

    return render(request,"coev/coevaluacion-vista-docente.html")

def coevAlm(request):

    return render(request, "coev/coevaluacion-vista-alumno.html")

def perfilVistaDueno(request):
    usuario=request.user
    cursos= Integrante_Curso.filter(rut__exact=usuario.username).objects.order_by('año').order_by('semestre')
    datosCurso=Curso.filter()


    #.filter(rut__exact=usuario.username)

    return render(request,"coev/perfil-vista-dueno.html",{'usuario':usuario, 'cursos':cursos})

def perfilVistaDoc(request):

    return render(request,"coev/perfil-alumno-vista-docente.html")