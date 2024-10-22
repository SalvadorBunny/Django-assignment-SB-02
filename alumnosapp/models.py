from django.db import models

# Create your models here.
class Alumnos(models.Model):
    alumno_nombre=models.CharField(max_length=50)
    alumno_fono=models.CharField(max_length=12)
    alumno_ingreso=models.CharField(max_length=12)
    alumno_carrera=models.CharField(max_length=30)
    alumno_observacion=models.CharField(max_length=500)