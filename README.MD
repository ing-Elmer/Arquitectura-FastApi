
##### Crear el entorno virtual

`python -m venv env1`

#### Activar entorno virtual

`./env1/Scripts/activate`

#### Instalar FastApi

`pip install fastapi uvicorn autopep8`

#### Registrar dependencia
`pip freeze > requirements.txt`

#### Ejecutar aplicacion

`uvicorn main:app --reload`

#### Instalar el conector a Sql

`pip install sqlalchemy `
* [Documentacion] (https://www.sqlalchemy.org/)

#### Instalar pyscopg2

`pip install pyscopg2`
* [Documentacion] (https://pypi.org/project/psycopg2/)


#### - Instalar dependencia Jinja2
* Instalar dependencia: pip install jinja2
* descripción: Jinja2 es un motor de plantillas para Python. Es rápido, ampliamente utilizado y seguro.
* Documentación oficial


#### Hashear la contraseña
`pip install passlib[bcrypt]`
* [Documentacion] (https://pypi.org/project/passlib/)
* [Documentacion] (https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

#### Instalar dependencia: pip install python-dotenv
* descripción: python-dotenv lee variables de entorno desde archivos .env.
* [Documentacion] https://pypi.org/project/python-dotenv/

#### - Instalar dependencia python-multipart
* Instalar dependencia: pip install python-multipart
* descripción: python-multipart es una librería para manejar datos multipart en Python.
* Documentación oficial
* Documentación Uploadfile
#### instalar valilador de correo 

`pip install validate_email_address`

#### instalar modulo de databases
`pip install fastapi[all] uvicorn databases`

#### enviar correos 

`pip install fastapi-mail`

#### JWT

`pip install "python-jose[cryptography]"`

* [Documentacion] (https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)


#### instalar dependencia para migraciones alembic
* instalar dependencia:pip install alembic 
* Documentación
#### Configuracion
* ⚠️La base de datos debe estar limpia, sin tablas
* Iniciar Alembic en el proyecto: alembic init alembic
* Ubicación de migraciones generadas: alembic/versions/
* Configurar archivo env.py
1: importar mis modelos
    # schema models
    from data.user_schema import UserSchema
    from data.category_task_schema import CategoryTaskSchema
2: Agregar url de conexión a base de datos
    config = context.config
    config.set_main_option('sqlalchemy.url',"driver://user:pass@localhost/dbname")
3: Agregar los shemas de los modelos a alembic
    target_metadata = {schemaModel1.metadata, schemaModel2.metadata}
Configurar archivo alembic.ini, agregando la url de conexión a bd sqlalchemy.url = driver://user:pass@localhost/dbname


Comandos alembic
Crear migración: alembic revision --autogenerate -m "nombre-migracion"
Aplicar la ultima migración: alembic upgrade head