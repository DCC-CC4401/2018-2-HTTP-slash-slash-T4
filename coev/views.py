from django.shortcuts import render , redirect
from .models import Curso
from .models import Equipo
from .models import Integrante_Equipo
from .models import Coevaluacion
from .models import Info_Coevaluacion
from .models import Integrante_Curso
from .models import Pendiente
from .models import User
from .forms import LoginForm
from .models import Pregunta
from itertools import chain
from  .forms import CoevForm
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
    coevs=Coevaluacion.objects.filter(curso=curso.id).filter(info_coevaluacion__usuario=request.user, info_coevaluacion__respondida=False)
    
    Resto=Coevaluacion.objects.filter(curso=curso.id).filter(info_coevaluacion__usuario=request.user,info_coevaluacion__respondida=True)
    print(Resto)
    return render(request, "coev/curso-vista-alumno.html",{'curso' : curso,'coevs':coevs,'resto':Resto, 'usuario':user})

def coevDoc(request,year,semestre,codigo,seccion,coev):

    user = request.user
    curso=Curso.objects.get(codigo=codigo,año=year,semestre=semestre,seccion=seccion)
    coev=Coevaluacion.objects.filter(curso=curso.id).get(numero=coev)
    return render(request,"coev/coevaluacion-vista-docente.html",{'curso' : curso,'coev':coev, 'usuario':user})

def coevAlm(request,year,semestre,codigo,seccion,coev, id_integrante=-1 ):
    user = request.user
    

    target = False
    bol = False
    curso=Curso.objects.get(codigo=codigo,año=year,semestre=semestre,seccion=seccion)
    coev=Coevaluacion.objects.filter(curso=curso.id).get(numero=coev)
    
    equipo=Equipo.objects.get(integrante_equipo__usuario=user, integrante_equipo__activo=True)
    integrantes=Integrante_Equipo.objects.filter(equipo=equipo).exclude(usuario=user)


    if id_integrante!=-1:        
        target = Integrante_Curso.objects.get(usuario__id=id_integrante)
        bol = True
    preguntas=Pregunta.objects.filter(coev=coev)
    if request.method == 'POST':
        print(request.POST['respondercoev'])
        
        hola= User.objects.get(id=request.POST['respondercoev'])
        print(hola)
        valor=  0.0
        total=len(list(preguntas.values('numero')))
        for pregunta in preguntas:            
            identificador=pregunta.id
            if pregunta.tipo:
                valor=float(request.POST.get('inlineRadioOptions'+str(pregunta.numero)))
                valor=valor
                newRespondida=Pendiente.objects.get(usuario=user, target=hola,coevaluacion=coev)

                newRespondida.notaTarget=valor
                newRespondida.pendiente=False
                newRespondida.save()
                infoT=Info_Coevaluacion.objects.get(usuario=hola,curso=curso, coevaluacion=coev)
                infoT.nota+=(valor-1)/total
                infoT.save()
                resp=list(Pendiente.objects.filter(usuario=user,target__in=integrantes.values('usuario'),pendiente=True ))
                if len(resp)==0:

                    infoU=Info_Coevaluacion.objects.get(usuario=user,curso=curso, coevaluacion=coev)
                    infoU.respondida=True
                    infoU.save()
    respondida=Pendiente.objects.filter(usuario=user,target__in=integrantes.values('usuario')).exclude(pendiente=False).values('target')
    listo=integrantes.exclude(usuario__in=respondida)
    return render(request, "coev/coevaluacion-vista-alumno.html", {'curso' : curso,'coev':coev,'preguntas':preguntas, 'usuario':user, 'equipo':equipo,'integrantes':integrantes,'listo':listo,'target':target, 'bol': bol})

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
