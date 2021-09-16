from django.db import models


# Create your models here.


class Paciente(models.Model):
    Nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=30)
    Cirurgia = models.CharField(max_length=50)
