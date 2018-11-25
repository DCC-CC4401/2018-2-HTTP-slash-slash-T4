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
from django.contrib.auth import authenticate, login, logout
from  .forms import CoevForm

def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = authenticate(username=form.cleaned_data['rut'],
                                   password=form.cleaned_data['clave'])
            if usuario is not None:
                login(request, usuario)
                if usuario.is_superuser:
                    return redirect('/admin/')
                return redirect('/home/alumnos')

        return render(request, "coev/login.html", {'form': LoginForm(), 'error': True})

    else:
        return render(request, "coev/login.html", {'form': LoginForm(), 'error': False})

def auth_logout(request):
        logout(request)
        return redirect('/')


def homeVistaAlum(request):
    user = request.user
    infoCoev = Info_Coevaluacion.objects.filter(usuario=request.user)
    infoCurso = Integrante_Curso.objects.filter(usuario=request.user)

    return render(request, "coev/home-vista-alumno.html",{'coev': infoCoev,
                                                          'cursos': infoCurso, 'usuario':user})


def homeVistaDoc(request):

    return render(request, "coev/home-vista-profesor.html")

def cursoVistaDoc(request,year,semestre,codigo,seccion):
    
    ramo=Curso.objects.get(codigo=codigo,año=year,semestre=semestre,seccion=seccion)
    validator=Integrante_Curso.objects.filter(curso=ramo).exclude(rol="Estudiante").filter(usuario=request.user)
    if validator:
        if request.method=='POST':
            if 'CursoAgregar' in request.POST:
                nuevaCoev=Coevaluacion()
                nuevaCoev.curso=ramo
                nuevaCoev.estado="Abierta"
                nuevaCoev.fecha_fin=request.POST['fecha_fin']
                nuevaCoev.fecha_inicio=request.POST['fecha_inicio']
                nuevaCoev.hora_fin=request.POST['hora_fin']
                nuevaCoev.hora_inicio=request.POST['hora_inicio']
                nuevaCoev.nombre=request.POST['nombreCoev']            
                infoCo = Coevaluacion.objects.filter(curso=ramo).order_by('numero')
                listaCoev=list(infoCo.values_list('numero', flat=True))
                if(not listaCoev):
                    nuevaCoev.numero=0
                else:
                    nuevaCoev.numero=listaCoev[-1]+1
                nuevaCoev.save()
            if 'pk' in request.POST:
                coev=Coevaluacion.objects.get(id=request.POST['pk'])
                print(request.POST['pk'])
                coev.estado="Publicada"
                coev.save()
        Coevs = Coevaluacion.objects.filter(curso=ramo).order_by('-numero')
        return render(request, "coev/curso-vista-docente.html",{'curso':ramo,'coevs':Coevs})
    else:
        return redirect('/home/alumnos')


def cursoVistaAlm(request,year,semestre,codigo,seccion):

    curso=Curso.objects.get(codigo=codigo,año=year,semestre=semestre,seccion=seccion)
    coevs=Coevaluacion.objects.filter(curso=curso.id).filter(info_coevaluacion__usuario=request.user).filter(info_coevaluacion__respondida=False)
    
    Resto=Coevaluacion.objects.filter(curso=curso.id).filter(info_coevaluacion__usuario=request.user).exclude(info_coevaluacion__respondida=False)

    return render(request, "coev/curso-vista-alumno.html",{'curso' : curso,'coevs':coevs,'resto':Resto})


def coevDoc(request):

    return render(request,"coev/coevaluacion-vista-docente.html")

def coevAlm(request):
    user = request.user

    return render(request, "coev/coevaluacion-vista-alumno.html", {'usuario': user})

def perfilVistaDueno(request):
    if not request.user.is_authenticated:
        redirect('/')
    cursos= Curso.objects.filter(integrante_curso__usuario=request.user.id)
    contexto= {'cursos': cursos}
    return render(request,"coev/perfil-vista-dueno.html", contexto)

def perfilVistaDoc(request):

    return render(request,"coev/perfil-alumno-vista-docente.html")