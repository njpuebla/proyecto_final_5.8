from django.db import models

# Create your models here.
class Electrica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

class Acustica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

class Amplificador(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50) 
    
class Efecto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)   