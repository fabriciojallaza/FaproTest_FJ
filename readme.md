# API para consultar la Unidad de Fomento en Python

###### Fapro API Test

Este proyecto consiste en una API que permite obtener el valor de la UF (Unidad de Fomento) chilena para una fecha determinada. El valor de la UF es obtenido desde el sitio web del Instituto Nacional de Estadísticas de Chile (INE) mediante web scrapping.

## Installation & Run

### Requerimientos para Windows o Linux
Requiere Python 3.7 o superior

~~~bash
sudo apt update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo apt-get install git-all
sudo apt-get install sqlite3
~~~


### Clonar el repositorio

~~~bash
# Mediante protocolo https
git clone https://github.com/fabriciojallaza/FaproTest_FJ.git

~~~

### Create virtualenv

~~~bash
python3 -m virtualenv venv
~~~

### Activar virtualenv

~~~bash
# For python >=3.10
source venv/local/bin/activate
# For python <3.10
source venv/bin/activate
~~~

### Instalar dependencias


#### Instalar requerimientos para virtualenv

~~~bash
pip install -r requirements.txt
~~~


#### Para correr los tests

~~~bash
python manage.py test
~~~

#### Correr el servidor

~~~bash
python manage.py runserver

# API Endpoint : http://127.0.0.1:8000
~~~


## Estructura del proyecto

```
FaproTest_FJ/
├── FaproTest_FJ/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── unidad_fomento/
├── lib/
│   │   ├── __init__.py
│   │   ├── uf_scrapper.py
│   │   └── validations.py    
├── utils/
│   │   └── months_spanish.py       
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── README.md
└── requirements.txt


2 directories, 19 files
```

## API
El método para obtener el valor de la UF se encuentra en la URL /uf/.

### Request
El valor de la fecha debe ser ingresado en el parámetro GET fecha con el formato YYYY-MM-DD.

~~~bash
http://localhost:8000/v1/uf?fecha=2022-05-05
~~~

### Response
La respuesta se entrega en formato JSON con el valor de la UF en la fecha especificada.

~~~json
{
    "uf_value": 32277.59
}
~~~

En caso de error, se entrega una respuesta con el código de error y un mensaje de error.
~~~json
{
     "error": "No se pudo obtener la UF para la fecha especificada."
}
~~~


### /v1/uf
* **GET**: Obten el valor de la UF para una fecha determinada

## Diseño de la arquitectura
La arquitectura de este proyecto sigue un patrón Modelo-Vista-Controlador (MVC), el cual permite separar la lógica de negocios de la lógica de presentación y de la interacción con el usuario.

El modelo es representado por la clase UFScrapper que se encarga de obtener los valores de la UF desde la página web del Banco Central de Chile, mediante técnicas de web scrapping. Además, esta clase utiliza la librería BeautifulSoup para analizar el contenido HTML de la página y extraer la información necesaria.

La vista es representada por la función get_uf_values en el archivo views.py, que se encarga de recibir las solicitudes HTTP y devolver las respuestas correspondientes. En este caso, se espera una solicitud GET con el parámetro "fecha" que representa la fecha de la UF que se desea obtener. Si la fecha es válida, se llama a la clase UFScrapper para obtener el valor de la UF y se devuelve en un objeto JSON.

El controlador es representado por la clase ValidationsUF en el archivo validations.py, que se encarga de validar las fechas ingresadas por el usuario. Esta clase verifica que la fecha cumpla con el formato "YYYY-MM-DD" y que la fecha no sea mayor a la fecha actual.

El proyecto también cuenta con un archivo de configuración llamado settings.py, que contiene todas las variables de configuración necesarias para la correcta ejecución del proyecto.

## Principios SOLID
En este proyecto se han utilizado varios principios SOLID de programación orientada a objetos, a continuación se detallan algunos de ellos:

* Principio de Responsabilidad Única (SRP): Cada clase tiene una única responsabilidad y no se encuentra sobrecargada con tareas adicionales que no le corresponden.
* Principio de Abierto/Cerrado (OCP): Las clases están abiertas para la extensión, pero cerradas para la modificación, esto se puede observar en la clase UFScrapper, la cual es fácilmente extensible para agregar nuevas funcionalidades sin necesidad de modificar su código existente.
* Principio de Inversión de Dependencias (DIP): Se han utilizado las librerías requests y BeautifulSoup para hacer el web scrapping, lo que permite que la clase UFScrapper no tenga dependencias directas con la implementación concreta de estas librerías, sino que sólo depende de sus interfaces públicas, lo que hace que la clase sea más fácil de mantener y extender.
* Principio de Sustitución de Liskov (LSP): En este proyecto se utilizó la clase padre datetime.date, la cual fue sustituida por la clase hija datetime.datetime.strptime, sin alterar el comportamiento esperado del programa.


Nota: Debido a la simplicidad del proyecto, no fue necesario aplicar todos los principios SOLID, sin embargo, se aplicaron aquellos que resultaron relevantes para el alcance del mismo.