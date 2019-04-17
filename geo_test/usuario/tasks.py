from background_task import background
from usuario.models import Usuario

####################################
##	Consulta los no geolocalizados
##	
##	Tarea ejecutada cada 1seg.
@background()
def geolocalizacion():
	user = Usuario.objects.geocodificar_usuarios()
	print(user)