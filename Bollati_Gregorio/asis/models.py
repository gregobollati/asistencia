# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
   

    def __str__(self):
        return 'Curso {}'.format(self.nombre)  

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    curso = models.ManyToManyField(Curso)

    def __str__(self):
        return 'Alumno {}'.format(self.nombre)

class Presencia(models.Model):
	fecha = models.DateTimeField()
	alumno = models.ForeignKey(Alumno)
	def __str__(self):
		return 'Alumno {} esta presente el dia {}'.format(self.alumno, self.fecha)