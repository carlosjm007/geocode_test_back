from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.templatetags.tz import localtime
'''
class UsuarioSerializer(serializers.ModelSerializer):
	usuario = serializers.SerializerMethodField('TraeUsuario')
	actualizado = serializers.SerializerMethodField('TraeActualizado')
	ideas = serializers.SerializerMethodField('TraeIdeas')
	def TraeUsuario(self, objeto):
		return "%s %s" % (objeto.usuario.first_name, objeto.usuario.last_name)
	def TraeActualizado(self, objeto):
		return "%s" % (localtime(objeto.actualizado).strftime("%d-%m-%y %I:%M %p"))
	def TraeIdeas(self, objeto):
		ideas = idea.objects.filter(tablero = objeto)
		serializer = IdeaSerializer(instance=ideas, many=True)
		return serializer.data
	class Meta:
		model = Usuario
		fields = ('id', 'usuario', 'estado', 'nombre', 'ideas', 'actualizado')
'''
class UsuarioCRUDSerializer(serializers.ModelSerializer):

	class Meta:
		model = Usuario
		fields = ('id', 'nombre', 'apellido', 'direccion', 'ciudad', 'longitud', 'latitud', 'estadogeo')
