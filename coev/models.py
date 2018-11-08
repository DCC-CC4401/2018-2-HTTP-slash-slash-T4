from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Curso(models.Model):
    nombre = models.charField(max_length=10)
    seccion = models.IntegerField(default=1)
    anho = models.integerField()
    semestre = models.integerField(
        validators=[MaxValueValidator(3), MinValueValidator(1)]
    )

    class Meta:
        unique_together = (("nombre", "seccion", "anho", "semestre"),)

    def __str__(self):
        return self.nombre + "-" + self.seccion + ", semestre" + self.semestre + self.anho


class Usuario(models.Model):
    rut = models.CharField(max_length=10,
                           primary_key=True,
                           null=False,
                           blank=False,
                           help_text='Ingrese rut sin puntos ni guión',
                           unique=True)
    nombre = models.CharField(null=False, blank=False)
    correo = models.EmailField(null=False, blank=False)


class Equipo(models.Model):
    curso_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(null=False, blank=False)
    historial = models.TextField(null=True, blank=True, unique=False)

    class Meta:
        unique_together = (("curso_id", "nombre"),)


class Integrante_Equipo(models.Model):
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = (("equipo_id", "curso_id", "rut"),)


class Admin(models.Model):
    usuario_rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Coevaluacion(models.Model):
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero = models.IntegerField(max_length=2, null=False, blank=False, unique=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    opciones = (("abierta", "Abierta"),
                ("cerrada", "Cerrada"),
                ("publicada", "Publicada"))
    estado = models.CharField(null=False, blank=False, choices=opciones)


class Info_Coevaluacion(models.Model):
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero = models.ForeignKey(Coevaluacion, to_field="numero", on_delete=models.CASCADE)
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    respondida = models.BooleanField(null=False)
    nota = models.FloatField(max_length=3, null=True, blank=True)

    class Meta:
        unique_together = (("curso_id", "numero", "rut"),)


class Integrante_Curso(models.Model):
    rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rol = models.charField(max_length=30)

    class Meta:
        unique_together = (("rut", "curso"),)

    def __str__(self):
        return self.rut
