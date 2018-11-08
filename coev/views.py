from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "coev/login.html")


def homeVistaAlum(request):
    return render(request, "coev/home-vista-alumno.html")


def homeVistaDoc(request):

    return render(request, "coev/home-vista-profesor.html")

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