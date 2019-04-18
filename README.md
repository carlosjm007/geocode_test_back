# Geocode test back

Para ejecutar el código se deben realizar los siguientes pasos:
  - Crear un entorno virtual con Python36.
  - Abrir una consola y entrar al entorno virtual.
  - Ejecutar el siguiente comando:
      geo_test/pip install -r requirements.txt
  - Realizar la carga de "seeds" o archivos iniciales con el siguiente comando:
      geo_test/python manage.py loaddata tasks.json
  - Ejecutar el comando para iniciar el servidor de manera local:
      geo_test/python manage.py runserver
  - Abrir otra consola dentro del entorno virtual y ejecutar el siguiente comando:
      geo_test/python manage.py process_tasks

# Propuesta

Se pretende monitorear la localización de usuarios utilizando dispositivos mixtos como celulares, gps, vehículos, entre otros.
Para lo anterior, se crea un servicio que sea capaz de almacenar, listar y eliminar usuarios, e incluso tambien lista aquellos usuarios cuya calidad de la información no es suficiente para dar con la ubicación del mismo.


![alt text](https://github.com/carlosjm007/geocode_test_back/blob/master/Sin%20t%C3%ADtulo.png "aja")

# Tarea programada

Se usó la librería [background_tasks](https://django-background-tasks.readthedocs.io/en/latest/) para ejecutar procedimientos cada cierto tiempo, de manera automática y transparente para el usuario.

En este caso, un proceso automático geocodoficará la dirección en caso de que las coordenadas de los usuarios no sean suministradas.

Lista de URLs:

| Solicitud HTTP | Endpoint | Descripción | Ejemplo |
| -- | -- | -- | -- |
| POST | /crear | Método que permite crear usuarios almacenando nombre, apellido dirección, ciudad y coordenadas en latitud y longitud(en caso de estar disponible). | ```{"nombre": "Ivan", "apellido": "Acosta", "direccion": "Cll 45 # 45 - 05", "ciudad": "Villavicencio", "latitud": 4.000, "longitud": -73.000}``` o ```{"nombre": "Ivan","apellido": "Acosta","direccion": "Cll 45 # 45 - 05","ciudad": "Villavicencio"}``` |
| GET | /lista | Método que retorna el listado de todos los usuarios con sus diferentes atributos. | -- |
| GET | /usuario/(identificador) | Método que recibe el ID de usuario y retorna el usuario con sus atributos. | -- |
| DELETE | /eliminar/(identificador) | Método que elimina el usuario identificado. | ```/eliminar/1/``` |
| GET | /geocodificar_base | Método que retorna una lista de los usuarios que no fueron geocodificados exitosamente por Google. | -- |

