from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q

# Create your views here.
class UsuarioList(APIView):
	def get(self, request, format=None):
		data = Usuario.objects.all()
		serializer = UsuarioCRUDSerializer(data, many=True)
		return Response(serializer.data)

class UsuarioCrear(APIView):
	def post(self, request, format=None):
		data = request.data
		serializer = UsuarioCRUDSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
	def get_object(self, pk):
		try:
			return Usuario.objects.get(pk=pk)
		except Usuario.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
	def get(self, request, pk, format=None):
		data = self.get_object(pk)
		serializer = UsuarioCRUDSerializer(data)
		return Response(serializer.data)

class UsuarioDelete(APIView):
	def get_object(self, pk):
		try:
			return Usuario.objects.get(pk=pk)
		except Usuario.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
	def delete(self, request, pk, format=None):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class geocodificar_base(APIView):
	def get(self, request, format=None):
		data = Usuario.objects.filter(Q(longitud=None, latitud=None) | Q(estadogeo=False) | Q(longitud=0.0, latitud=0.0))
		serializer = UsuarioCRUDSerializer(data, many=True)
		return Response(serializer.data)