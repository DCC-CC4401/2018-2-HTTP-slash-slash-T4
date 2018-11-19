from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    seccion = models.IntegerField(default=1)
    año = models.IntegerField()
    opciones = (("Primavera", "Primavera"),
                ("Otoño", "Otoño"),
                ("Verano", "Verano"))
    semestre = models.CharField(choices=opciones, max_length=30, null=False, blank=False, default=opciones[0][0])
    codigo = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        unique_together = (("codigo", "seccion", "año", "semestre"),)

    def __str__(self):
        return self.nombre + " " + str(self.año) + ", " + str(self.semestre)


class Equipo(models.Model):
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    historial = models.TextField(null=True, blank=True, unique=False)

    class Meta:
        unique_together = (("curso_id", "nombre"),)

    def __str__(self):
        return self.nombre + " | " + str(self.curso_id)


class Integrante_Equipo(models.Model):
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    rut = models.ForeignKey(models.User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = (("equipo_id", "rut"),)

    def __str__(self):
        return str(self.rut)


class Admin(models.Model):
    usuario_rut = models.ForeignKey(models.User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario_rut)

class Coevaluacion(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank= True)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99)], null=False, blank=False, unique=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    opciones = (("Abierta", "Abierta"),
                ("Cerrada", "Cerrada"),
                ("Publicada", "Publicada"))
    estado = models.CharField(max_length=20, null=False, blank=False, choices=opciones)

    def __str__(self):
        return "Coevaluación " + str(self.numero)


class Info_Coevaluacion(models.Model):
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    coevaluacion_id = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE)
    rut_usuario = models.ForeignKey(models.User, on_delete=models.CASCADE)
    respondida = models.BooleanField(null=False)
    nota = models.FloatField(max_length=3, null=True, blank=True)

    class Meta:
        unique_together = (("curso_id", "coevaluacion_id", "rut_usuario"),)

    def __str__(self):
        return str(self.rut_usuario) + " " + str(self.nota)

class Integrante_Curso(models.Model):
    rut = models.ForeignKey(models.User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    opciones = (("Ayudante", "Ayudante"),
                ("Profesor/a", "Profesor/a"),
                ("Auxiliar", "Auxiliar"),
                ("Estudiante", "Estudiante"))
    rol = models.CharField(max_length=20, null=False, blank=False, choices=opciones)

    class Meta:
        unique_together = (("rut", "curso"),)

    def __str__(self):
        return str(self.rut)
