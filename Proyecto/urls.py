"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from coev import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.auth_login, name='login'),
    path('home/alumnos' ,views.homeVistaAlum, name='homeAlumnos'),
    path('home/docentes',views.homeVistaDoc, name='homeDocentes'),

    path('docentes/curso/<int:year>/<int:semestre>/<str:codigo>/<int:seccion>',views.cursoVistaDoc, name='cursoDocentes'),
    path('docentes/curso/<int:year>/<int:semestre>/<str:codigo>/<int:seccion>/<int:coev>', views.coevDoc, name='coevDocentes'),
    path('curso/<int:year>/<int:semestre>/<str:codigo>/<int:seccion>/<int:coev>/<int:id_integrante>',views.coevAlm, name='respondercoev'),
    path('curso/<int:year>/<int:semestre>/<str:codigo>/<int:seccion>/<int:coev>',views.coevAlm, name='coevalumnos'),
    path('perfil',views.perfilVistaDueno, name='perfilDueno'),
    path('docentes/perfil', views.perfilVistaDoc, name='perfilDocente'),
    path('curso/<int:year>/<int:semestre>/<str:codigo>/<int:seccion>',views.cursoVistaAlm, name='cursoAlumnos'),
    path('logout', views.auth_logout, name='logout'),
    path('cambiar_clave', views.cambiarClave, name='cambiarClave'),
    path('coevaluacion/<int:id>/', views.fichaCoev, name='fichaCoevAlumnos'),
]
