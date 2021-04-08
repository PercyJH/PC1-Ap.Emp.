from django.db import models

# Create your models here.

class Region(models.Model):
    region_opcion = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Opcion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    candidato = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
