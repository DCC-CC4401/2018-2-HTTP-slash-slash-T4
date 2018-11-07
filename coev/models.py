from django.db import models

# Create your models here.
class Integrante_Curso(models.Model):
    rut=models.ForeignKey(Usuario)
    curso=models.ForeignKey(curso.id)
    rol=models.charField(max_length=30)
        def __str__(self):
        return self.rut
        
