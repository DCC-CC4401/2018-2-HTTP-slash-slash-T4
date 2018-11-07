from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Integrante_Curso(models.Model):

    rut=models.ForeignKey(Usuario)
    curso=models.ForeignKey(curso.id)
    rol=models.charField(max_length=30)
    class Meta:
        unique_together=(("rut","curso"),)
    def __str__(self):
        return self.rut

class curso(models.Model):
    nombre=models.charField(max_length=10)
    seccion=models.IntegerField(default=1)
    anho=models.integerField()
    semestre=models.integerField(
        validators=[MaxValueValidator(3), MinValueValidator(1)]
    )
    class Meta:
        unique_together=(("nombre","seccion","anho","semestre"),)
    def __str__(self):
        return self.nombre"-"+self.seccion", semestre"+self.semestre+self.anho
