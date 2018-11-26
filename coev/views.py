from django.shortcuts import render , redirect
from .models import Curso
from .models import Equipo
from .models import Integrante_Equipo
from .models import Admin
from .models import Coevaluacion
from .models import Info_Coevaluacion
from .models import Integrante_Curso
from .models import Pendiente
from .forms import LoginForm
from django.http import HttpResponseRedirect
from itertools import chain
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
    coev=1
    bol=False
    user = request.user
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
                coev.estado="Publicada"
                coev.save()
            if 'edit' in request.POST:                
                coev=Coevaluacion.objects.get(id=request.POST['edit'])
                bol=True
            if 'ModificarCoev' in request.POST:
                coev=Coevaluacion.objects.get(id=request.POST['ModificarCoev'])
                coev.fecha_fin=request.POST['fecha_fin']
                coev.fecha_inicio=request.POST['fecha_inicio']
                coev.hora_fin=request.POST['hora_fin']
                coev.hora_inicio=request.POST['hora_inicio']
                coev.nombre=request.POST['nombreCoev']
                coev.save()
        Coevs = Coevaluacion.objects.filter(curso=ramo).order_by('-numero')
        return render(request, "coev/curso-vista-docente.html",{'curso':ramo,'coevs':Coevs, 'usuario':user,'coev':coev,'bol':bol})
    else:
        return redirect('/home/alumnos')


def cursoVistaAlm(request,year,semestre,codigo,seccion):
    
    user = request.user
    curso=Curso.objects.get(codigo=codigo,año=year,semestre=semestre,seccion=seccion)
    coevs=Coevaluacion.objects.filter(curso=curso.id).filter(info_coevaluacion__usuario=request.user).filter(info_coevaluacion__respondida=False)
    
    Resto=Coevaluacion.objects.filter(curso=curso.id).filter(info_coevaluacion__usuario=request.user).exclude(info_coevaluacion__respondida=False)

    return render(request, "coev/curso-vista-alumno.html",{'curso' : curso,'coevs':coevs,'resto':Resto, 'usuario':user})


def coevDoc(request,year,semestre,codigo,seccion,coev):

    user = request.user
    curso=Curso.objects.get(codigo=codigo,año=year,semestre=semestre,seccion=seccion)
    coev=Coevaluacion.objects.filter(curso=curso.id).get(numero=coev)
    return render(request,"coev/coevaluacion-vista-docente.html",{'curso' : curso,'coev':coev, 'usuario':user})

def coevAlm(request,year,semestre,codigo,seccion,coev):
    user = request.user
    curso=Curso.objects.get(codigo=codigo,año=year,semestre=semestre,seccion=seccion)
    coev=Coevaluacion.objects.filter(curso=curso.id).get(numero=coev)
    equipo=Equipo.objects.get(integrante_equipo__usuario=user, integrante_equipo__activo=True)
    integrantes=Integrante_Equipo.objects.filter(equipo=equipo).exclude(usuario=user)
    respondida=Pendiente.objects.filter(usuario=user,target__in=integrantes.values('usuario')).exclude(pendiente=False).values('target')
    listo=integrantes.exclude(usuario__in=respondida)
    print(listo)
    print("\n")
    print(integrantes)
    return render(request, "coev/coevaluacion-vista-alumno.html", {'curso' : curso,'coev':coev, 'usuario':user, 'equipo':equipo,'integrantes':integrantes,'listo':listo})

def perfilVistaDueno(request):
    if not request.user.is_authenticated:
        redirect('/')
    cursos= Curso.objects.filter(integrante_curso__usuario=request.user.id)
    contexto= {'cursos': cursos}
    return render(request,"coev/perfil-vista-dueno.html", contexto)

def perfilVistaDoc(request):

    return render(request,"coev/perfil-alumno-vista-docente.html")