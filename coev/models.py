from django.db import models

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
    semestre=models.integerField()
    def __str__(self):
        return self.nombre"-"+self.seccion", semestre"+self.semestre+self.anho