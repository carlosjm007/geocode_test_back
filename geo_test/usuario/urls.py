from django.urls import include, path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('lista/', UsuarioList.as_view(), name='usuario-list'),
	path('crear/', UsuarioCrear.as_view(), name='usuario-crear'),
	path('usuario/<int:pk>/', UsuarioDetail.as_view()),
	path('eliminar/<int:pk>/', UsuarioDelete.as_view()),
	path('geocodificar_base/', geocodificar_base.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)