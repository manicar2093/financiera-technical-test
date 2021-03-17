# Financiero. Prueba técnica

Este repositorio contiene el código de respuesta para la prueba técnica que se solicitó.

# Tests

Para correr los tests es necesario contar con unittest que fue la libreria que se uso para este proposito.

Usando el siguiente comando dentro del path del priyecto se podrá corres las pruebas en general con los detalles de cada prueba.
```
python -m unittest -v
```

# Iniciar proyecto

Para iniciar este proyecto primero se deben instalar las dependencias usando el siguiente comando:
```
pip install -r requirements.txt
```

Después de esto, es necesario declarar algunas variables de ambiente:

- APP_ENVIROMENT: indica la configuración que se usará y hay doc disponibles= "app.config.local" y "app.config.prod"
- FLASK_APP: indica la aplicacion con la que se trabajara. En este caso es con autoapp.py

Al tener esto configurado se corre el comando:
```
flask run
```

# Endpoint

Esta API solo cuenta con 3 endpoints:

- __/inmem__ __PUT__: A través de ella se puede registrar un nuevo valor con su llave proporcionando el siguiente JSON:
```
{
    "key": "aKey",
    "value": "Manuel"
}
```

Y regresa la siguiente respuesta:
```
{
    "key": "aKey",
    "value": "aValue",
    "version": 1
}
```
NOTA: El key y el value son requeridos. En caso de no contener alguno de los dos se responderá con el siguiente JSON:
```
{
    "message": "Key not found in body. Consider request's documentation"
}
```
O con:
```
{
    "message": "Value not found in body. Consider request's documentation"
}
```

- __/inmem/{key}__ __GET__: Realiza la busqueda por el key proporcionado. Regresa el siguiente JSON:
```
{
    "key": "aKey",
    "value": "aValue",
    "version": 1
}
```

- __/inmem/{key}/{version}__ __GET__: Realiza la busqueda por el key y versión proporcionado. Regresa el siguiente JSON:
```
{
    "key": "aKey",
    "value": "aValue",
    "version": 1
}
```