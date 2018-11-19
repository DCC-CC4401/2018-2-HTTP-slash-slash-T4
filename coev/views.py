from django.shortcuts import render , redirect
from .models import Curso
from .models import Usuario
from .models import Equipo
from .models import Integrante_Equipo
from .models import Admin
from .models import Coevaluacion
from .models import Info_Coevaluacion
from .models import Integrante_Curso

# Create your views here.


def index(request):
    return render(request, "coev/login.html")


def homeVistaAlum(request):
    return render(request, "coev/home-vista-alumno.html")


def homeVistaDoc(request):
    coevaluaciones = Coevaluacion.objects.order_by('fecha_inicio')
    return render(request, "coev/home-vista-profesor.html", {'coev': coevaluaciones})



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