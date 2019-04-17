from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.templatetags.tz import localtime

class UsuarioCRUDSerializer(serializers.ModelSerializer):

	class Meta:
		model = Usuario
		fields = ('id', 'nombre', 'apellido', 'direccion', 'ciudad', 'longitud', 'latitud', 'estadogeo')
