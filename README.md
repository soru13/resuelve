# resuelve

Resuelve.mx 
Numero de facturas por cliente dado un id


Opción 1 (a través de un pequeño servidor web levantado localmente)

	Dependencias:
		-paso 1 instalar PIP <- pip es un gestor de repositorios para python
		//Mac OS
		sudo easy_install pip   
		//Para Ubuntu, Debian o Linux Mint.
		sudo apt-get install python-pip 
		//Fedora
		sudo yum install python-pip
		//windows
		https://bootstrap.pypa.io/get-pip.py <-guardamos el contenido y luego ejecuta python get-pip.py

		-Paso 2 instalar Flask

		"""Flask ("un pequeño motorcito") es un framework minimalista escrito en python y basado en las espesificación WSGI de Werkzeug y el motor de templates jinja2. Tienela licenciaBSD."""

		sudo pip install Flask

		-Paso 3 hasta aquí ya podemos correrlo

		python con_flask.py

		//para salir
		ctrl + C

Opción 2 (En consola, con un poquito menos de código)

	//solo corre esto:
	python numero_faturas.py
	
	//para salir
	ctrl + C

Análisis o lógica
	//1 por meses:
		tratara de buscar por meses ejemplo: enero(31) 2017-01-01  | 2017-01-31 , febrero(28) 2017-02-01  | 2017-02-28, etc.
		Si un mes exede los 100 resultados el código tratara de hacerlo por semanas
	//2 por semanas:
		Tratara de resolverlo por semanas. Sino por dias.
	//3 Días:
		Lo resolvera por dias cuando detecta que no hes ni la semana el rango de fechas a buscar."""
Postdata
	AL analisar el código se darann cuenta que interactuo con las fechas y por falta de tiempo no pude optimizarlo más, el código es capas de resolverlo por meses, semanas y días. Pero como es un repositorio publico otra persona lo puede usar y continuar optimizandolo como ejemplo:
	Si hay 6 meses a buscar y 2 de ellos exede las 100 facturas, entonces 4 de ellos se buscara por rango e fechas por mes y los otros dos continuaran sumando facturas pero por semanas.


