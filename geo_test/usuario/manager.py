from django.db import models
import json, requests, time, urllib3
from django.utils import timezone
from django.db.models import Q
from django.conf import settings

class UsuarioManager(models.Manager):
	############################################
	###	metodo que geocodifica los usuarios
	def geocodificar_usuarios(self):
		usuario = self.filter(estadogeo=False).first()
		if usuario == None:
			print("No existen usuarios para geolocalizar")
			return None
		variables = urllib3.request.urlencode(
			{
				"address" : "%s,%s,colombia"%(usuario.direccion, usuario.ciudad),
				"key" : "%s"%(settings.GOOGLE_KEY)
			}
		)
		url = '%s?%s'%(settings.GOOGLE_API, variables)
		solicitud = requests.get(url).json()
		if solicitud["status"] != "OK":
			usuario.latitud = 0.0
			usuario.longitud = 0.0
			usuario.estadogeo = True
			usuario.save()
			return None
		usuario.latitud = solicitud["results"][0]["geometry"]["location"]["lat"]
		usuario.longitud = solicitud["results"][0]["geometry"]["location"]["lng"]
		usuario.estadogeo = True
		usuario.save()
		return usuario