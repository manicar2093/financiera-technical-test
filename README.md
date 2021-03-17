# Financiero

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