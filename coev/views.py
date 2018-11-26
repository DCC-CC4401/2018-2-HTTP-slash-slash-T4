from django.shortcuts import render , redirect
from .models import Curso
from .models import Equipo
from .models import Integrante_Equipo
from .models import Coevaluacion
from .models import Info_Coevaluacion
from .models import Integrante_Curso
from .forms import LoginForm
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import json



def auth_login(request):
    if request.user.is_authenticated:
        return redirect('/home/alumnos')
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
                                                          'cursos': infoCurso, 
                                                          'usuario':user})

def homeVistaDoc(request):

    return render(request, "coev/home-vista-profesor.html")


def cursoVistaDoc(request):

    return render(request, "coev/curso-vista-docente.html")


def cursoVistaAlm(request):

    return render(request, "coev/curso-vista-alumno.html")

def coevDoc(request):

    return render(request,"coev/coevaluacion-vista-docente.html")


def coevAlm(request):
    user = request.user
    infoCoev = Info_Coevaluacion.objects.filter(usuario=request.user)

    return render(request, "coev/coevaluacion-vista-alumno.html", {'usuario': user,'coev': infoCoev})


def perfilVistaDueno(request):
    if not request.user.is_authenticated:
        redirect('/')
    cursos= Curso.objects.filter(integrante_curso__usuario=request.user.id)
    for curso in cursos:
        curso.info_coevaluaciones= Info_Coevaluacion.objects.filter(usuario= request.user.id,
                                                                    curso= curso.id,
                                                                    coevaluacion__estado='Publicada')
    contexto= {'cursos': cursos}
    return render(request,"coev/perfil-vista-dueno.html", contexto)


def perfilVistaDoc(request):

    return render(request,"coev/perfil-alumno-vista-docente.html")


def cambiarClave(request):
    if not request.user.is_authenticated or request.method != 'POST':
        return JsonResponse({'ok': False})
    usuario= authenticate(username=request.user.get_username(),password=request.POST['clave-antigua'])
    if usuario is not None:
        usuario.set_password(request.POST['clave-nueva'])
        usuario.save()
        update_session_auth_hash(request, usuario)
        return JsonResponse({'ok': True})
    else:
        return JsonResponse({'ok': False})


def fichaCoev(request,id):
    info = Info_Coevaluacion.objects.filter(coevaluacion__id=id).first()
    user = request.user
    integrante1 = Integrante_Equipo.objects.filter(usuario=user).first()
    if integrante1 is None:
        raise Http404("Poll does not exist")
    integrantes = Integrante_Equipo.objects.filter(equipo=integrante1.equipo)

    return render(request, "coev/coevaluacion-vista-alumno.html", {'infoCoev': info, 'usuario':user, 'integrantes':integrantes, 'equipo': integrante1.equipo})
