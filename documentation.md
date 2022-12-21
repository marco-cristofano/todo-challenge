# Invera ToDo-List Challenge


El presente documento contiene la información relevante relacionada a la aplicación ToDo-List

## Funcionalidad:

Si bien el enunciado detalla los requerimientos de la aplicación, a continuación se listan algunas interpretaciones y decisiones con respecto al mismo:

1. Además de la creación y eliminación de una tarea se pedía "Marcar tareas como completadas". Se desarrolló un CRUD completo y agregarle un endpoint que solo pasa a estado completada la tarea en cuestión. 

2. Con respecto a la autenticación en la charla inicial se me comentó que era una buena idea implementarla con Oauth. Por lo tanto se implementó Oauth dentro del mismo proyecto (no se consumen servicios de google, github, twitter, etc).

3. Se requería permitir la búsqueda por "fecha creación y/o por el contenido de la misma". Considerando que el modelado de una tarea posee un título, una descripción, fecha de creación, fecha y hora de última actualización, el estado (completada o no) y usuario, la búsqueda se posibilita por fecha de creación, descripción y título. 

4. Cada usuario solo puede ver, editar, marcar como completadas  y eliminar sus propias tareas.

5. Las tareas poseen borrado lógico.


## Infraestructura:

- El backend fue realizado con Django (3.2.16), Django Rest Framework (3.14.0 Versión más actual al día de la fecha).

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

 Todos los endpoints se encuentran protegidos, es decir, requieren usuarios autenticados.

### Obtención del access_token

curl -X POST -d "grant_type=password&username=<USER>&password=<PASSWORD>" -u"client_id:client_secret" http://localhost:8080/o/token/

Para ello se puede utilizar un usuario creado por defecto (credenciales user user):

curl -X POST -d "grant_type=password&username=user&password=user" -u"client_id:client_secret" http://localhost:8080/o/token/
  
### Creación de un usuario

Si no se desea utilizar un usuario de los creados automáticamente, se provee siguiente endpoint para crear uno:

curl -X POST -d "username=<USER>&password=<PASSWORD>" http://localhost:8080/user/
  
Por ejemplo:

curl -X POST -d "username=user3&password=user3" http://localhost:8080/user/
  
### Listado de tareas
curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://localhost:8080/api/to_do/
  
Por ejemplo:
 
curl -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR" http://localhost:8080/api/to_do/
 

### Búsqueda de tareas

Para las búsqueda de tareas se deben enviar los parámetros en la url. Los tres parámetros aceptados son: title, description y created. Se puede buscar por un solo parámetro o cualquier combinación deseada:

Por ejemplo:
 
curl -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR" http://localhost:8080/api/to_do/?description=descripcion1
 
Si se busca por fecha se debe respetar el formato 'YYYY-MM-DD'
 
Por ejemplo:
 
curl -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR" http://localhost:8080/api/to_do/?created=2022-12-19

 
### Creación de una tarea
 
 La creación de una tarea admite tres campos: title, description y completed. 
 
 - title: campo obligatorio.
 
 - description: campo opcional.

 - completed: campo opcional. Si no se envia por defecto es false.
 
 Los campos created, last_modification y user se manejan de manera transparente al usuario.
 
curl -X POST  -H "Authorization: Bearer <ACCESS_TOKEN>" -d "title=<TITULO>&description=<DESCRIPCION>&completed=<true/false>"  http://localhost:8080/api/to_do/
 
 Por ejemplo:
 
curl -X POST  -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR" -d "title=titulo_nuevo&description=descripcion_nueva&completed=true"  http://localhost:8080/api/to_do/

 
 ### Actualización de una tarea
 
 La actualización de una tarea admite tres campos: title, description y completed. 
 
 - title: campo obligatorio.
 
  curl -X PUT  -H "Authorization: Bearer <ACCESS_TOKEN>" -d "title=<NUEVO_TITULO>&description=<NUEVA_DESCRIPCION>&completed=<trues/false>"  http://localhost:8080/api/to_do/<ID>/
 
 Por ejemplo:
 
 curl -X PUT  -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR" -d "title=titulo_nuevo1&description=descripcion_nueva1&completed=false"  http://localhost:8080/api/to_do/8/

 
  ### Marcar como completada una tarea
 
  curl -X PUT  -H "Authorization: Bearer <ACCESS_TOKEN>"  http://localhost:8080/api/to_do/<ID>/completed/
 
 Por ejemplo:
 
 curl -X PUT  -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR"  http://localhost:8080/api/to_do/8/completed/

 ### Eliminar una tarea
 
 curl -X DELETE  -H "Authorization: Bearer <ACCESS_TOKEN>"  http://localhost:8080/api/to_do/<ID>/
 
 Por ejemplo:
 
 curl -X DELETE  -H "Authorization: Bearer 3NyAOIPXMPjdWz0GpiQIZSPUWNislR"  http://localhost:8080/api/to_do/8/

 
## Comentarios del código fuente:
 
- Posee cobertura del 100% (sobre las líneas desarrolladas).

- Si bien por la dimensión del proyecto no se necesariamente se justifica, la lógica de negocio de cada aplicación es almacenada en servicios.
 
- El manejo de URL se puede cambiar. Al ser un desarrollo pequeño se encuentra en el propio archivo urls brindado por Django, si el proyecto creciera sería aconsejable:
    - Opción 1:  Llevar el manejo de urls de la api a una carpeta específica. 
    - Opción 2: Delegar el manejo de urls a cada aplicación.
 
- El cdigo fue analizado con safety (versión gratuita) y bandit en busca de vulnerabilidades. 
