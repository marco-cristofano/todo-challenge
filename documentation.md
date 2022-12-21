# Invera ToDo-List Challenge


El presente documento contiene la información relevante relacionada a la aplicación ToDo-List

## Funcionalidad:

Si bien el enunciado detallaba los requerimientos de la aplicación, a continuación se listan algunas interpretaciones y decisiones con respecto al mismo:

1. Además del la creacion y eliminación de una tarea se pedía "Marcar tareas como completadas". Se desarrolló un CRUD completo y agregarle un endpoint que solo pasa a estado completada la tarea en cuestión. 

2. Con respecto a la autenticación en la charla inicial se me comentó que era una buena idea implemenmtarla con Oauth. Por lo tanto se implementó Oauth dentro del mismo proyecto (no se consume servicios de google, github, twitter, etc).

3. Se requería permitir la búsqueda por "fecha creación y/o por el contenido de la misma". Considerando que el modelado de una tarea posee un titulo, una descripción, fecha de creacion, fecha y hora de ultima actualizacion, el estado (completada o no) y usuario, la búsqueda se posibilita por fecha de creacion, descripcion y titulo. 

4. Cada usuario solo puede ver, editar, marcar como completadas  y eliminar sus propias tareas.


## Infraestructura:

- El backend fue realizado con Django (3.2.14 LTS), Django Rest Framework (3.14.0 Versión mas actual al dia de la fecha).

- La base de datos es PostgreSQL.

- Servidor Web Nginx 1.23.3 (escuchando el puerto 8080)

Toda la infraestructura se encuentra dockerizada.

## Puesta en marcha del proyecto

Para levantar el proyecto es necesario tener instalado docker y docker-compose. Si listan los pasos levantarlo

1. Ir a la carpeta "docker"

2. docker-compose build

3. docker-compose up

* si es la primera vez que se enciende puede que el servicio "todo_challenge_backend" levante antes que "todo_challenge_db" termine su inicialización y al intentarse conectar falle y se caiga. Si esto sucede volver a ejecutar el paso 3.

Al levantar el backend carga en la BDD la información necesaria para el correcto funcionamiento de Oauth, dos usuarios de prueba y 4 tareas.


## Endpoints disponibles

 Todos los endpoints se encuentran protegidos, es decir, requieren usuarios atenticados.

### Obtención del access_token

curl -X POST -d "grant_type=password&username=<USER>&password=<PASSWORD>" -u"client_id:client_secret" http://localhost:8080/o/token/

Para ello se puede utilizar un usuario creado por defecto (credenciales user user):

curl -X POST -d "grant_type=password&username=user&password=user" -u"client_id:client_secret" http://localhost:8080/o/token/
  
### Creacion de un usuario

Si no se desea utilizar un usuaio de los creados automaticamente, se provee siguiente endpoint para crear uno:

curl -X POST -d "username=<USER>&password=<PASSWORD>" http://localhost:8080/user/
  
Por ejemplo:

curl -X POST -d "username=user3&password=user3" http://localhost:8080/user/
  
### Listado de tareas
curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://localhost:8080/api/to_do/
  
Por ejmeplo:
 
curl -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR" http://localhost:8080/api/to_do/



