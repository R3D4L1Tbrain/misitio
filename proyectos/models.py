from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=10000)
    tecnologias = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)


