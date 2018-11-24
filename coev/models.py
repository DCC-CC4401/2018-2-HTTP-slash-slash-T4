from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    seccion = models.IntegerField(default=1)
    año = models.IntegerField()
    opciones = ((1, "Otoño"),
                (2, "Primavera"),
                (3, "Verano"))
    semestre = models.IntegerField(choices=opciones, null=False, blank=False)
    codigo = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        unique_together = (("codigo", "seccion", "año", "semestre"),)

    def __str__(self):
        return self.nombre + " " + str(self.año) + ", " + str(self.semestre)


class Equipo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    historial = models.TextField(null=True, blank=True, unique=False)

    class Meta:
        unique_together = (("curso", "nombre"),)

    def __str__(self):
        return self.nombre + " | " + str(self.curso_id)


class Integrante_Equipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = (("equipo", "usuario"),)

    def __str__(self):
        return str(self.usuario)


class Admin(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario)

class Coevaluacion(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank= True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99)], null=False, blank=False, unique=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    opciones = (("Abierta", "Abierta"),
                ("Cerrada", "Cerrada"),
                ("Publicada", "Publicada"))
    hora_inicio = models.TimeField(null=False,blank=False, default=timezone.now)
    hora_fin = models.TimeField(null=False,blank=False, default=timezone.now)
    estado = models.CharField(max_length=20, null=False, blank=False, choices=opciones)

    def __str__(self):
        return "Coevaluación " + str(self.numero)


class Info_Coevaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    coevaluacion = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    respondida = models.BooleanField(null=False)
    nota = models.FloatField(max_length=3, null=True, blank=True)

    class Meta:
        unique_together = (("curso", "coevaluacion", "usuario"),)

    def __str__(self):
        return str(self.usuario) + " " + str(self.nota)

class Integrante_Curso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    opciones = (("Ayudante", "Ayudante"),
                ("Profesor/a", "Profesor/a"),
                ("Auxiliar", "Auxiliar"),
                ("Estudiante", "Estudiante"))
    rol = models.CharField(max_length=20, null=False, blank=False, choices=opciones)

    class Meta:
        unique_together = (("usuario", "curso"),)

    def __str__(self):
        return str(self.usuario)
