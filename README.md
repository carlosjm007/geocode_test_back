# geocode_test_back

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
