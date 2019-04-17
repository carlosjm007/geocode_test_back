from django.db import models
from .manager import UsuarioManager

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	ciudad = models.CharField(max_length=255)
	longitud = models.FloatField(null=True, blank=True)
	latitud = models.FloatField(null=True, blank=True)
	estadogeo = models.BooleanField(default=False)
	objects = UsuarioManager()
	def __str__(self):
		return "%s - %s" %(self.nombre, self.ciudad)

	##########################
	##	Se valida si existen los campos latitud y longitud fueron suministrados
	def save(self, *args, **kwargs):
		if self.latitud != None and self.longitud != None:
			self.estadogeo = True
		super(Usuario, self).save(*args, **kwargs)