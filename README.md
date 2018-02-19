# StringTagger - Clasificación de Texto

"StringTagger" es el nombre que le he dado a este proyecto. Se trata de un modulo que implementa un clasificador bayesiano simple para la clasificación de cadenas de textos.

Puedes descargar StringTagger ingresando al siguiente enlace: https://github.com/LuisAlejandroSalcedo/StringTagger-Clasificador-de-Texto.

La analogía es muy simple, el clasificador clasificara las cadenas de texto según el numero de las palabras más frecuentes.  Lo primero que debemos hacer para poner en funcionamiento el clasificador, es entrenarlo. La forma en la que entrenamos al clasificador es dándole largos contenidos de texto, luego este los dividirá en palabras para saber cuales son las palabras más frecuentes, de esta manera a las nuevas cadenas de texto podrá clasificarlas según la frecuencia de palabras.

¿Un ejemplo? Claro, aquí lo tenemos: ([clasificador_de_texto_ejemplo.py](https://github.com/LuisAlejandroSalcedo/StringTagger-Clasificador-de-Texto/blob/master/clasificador_de_texto_ejemplo.py))



```python
"""
Uso sencillo de "StringTagger" para el etiquetado (clasificación) de texto.
"""

__author__ = "Luis Salcedo" 

from StringTagger.StringClf import Classifier
from StringTagger.getPage import getTextPage

training_data = { # Datos para entrenar al clasificador
	"Ciencia":[
		'https://es.wikipedia.org/wiki/Ciencia', # Entrenamos al clasificador con paginas de wikipedia.
		'https://es.wikipedia.org/wiki/Qu%C3%ADmica'
	],
	"Deportes":[
		'https://es.wikipedia.org/wiki/Deporte',
		'https://es.wikipedia.org/wiki/Deportes_ol%C3%ADmpicos'
	],
	"Tecnologia":[
		'https://es.wikipedia.org/wiki/Tecnolog%C3%ADa',
		'https://es.wikipedia.org/wiki/Rob%C3%B3tica'
	],
	
}

clf = Classifier() # Instancia del clasificador

for category,urls in training_data.items(): # Entrenamos al clasificador con el contenido de cada pagina
	for url in urls:
		clf.train(getTextPage(url),category) # El metodo "getTextPage", recive como argumento una url para extraer su texto

# Iniciamos el proceso de clasificación con el metodo "String"
# Solo le pasamos como argumento el texto que deseamos etiquetar (clasificar)
string = "Molécula de agua, dos átomos de hidrógeno unidos a uno de oxígeno."
clas = clf.String(string)
print('\n')
print("Texto: %s " % string)
print("Etiqueta del Texto: %s" % clas)
```
El código anterior nos muestro el uso básico de "StringTagger", como se puede apreciar, lo primero que se hace es crear un diccionario, el cual contiene el nombre de todas las categorías. Cada categoría contiene un par de url, a las cuales el método "getTextPage" extrae todo su texto y lo usa para el entrenamiento del clasificador. 

Luego de entrenar al clasificador, utilizamos el método "String" para clasificar el texto que ingrese el usuario. El método "String" de la clase "Classifier" nos devolverá el nombre de la categoría a la cual pertenezca el texto.

El resultado del ejemplo anterior seria:

![Resultado del clasificador](https://github.com/LuisAlejandroSalcedo/StringTagger-Clasificador-de-Texto/blob/master/resultado_clasificador_ejemplo.PNG)

Puedes descargar StringTagger y el ejemplo anterior ingresando al siguiente enlace: https://github.com/LuisAlejandroSalcedo/StringTagger-Clasificador-de-Texto.

Como se puede observar en la imagen, el script extrae todo el texto de las paginas web que les proporcionamos, para que luego este aprenda de los textos.  Luego le pasamos una cadenas de texto, para luego obtener el resultado que este caso es "Ciencia".

(Si se preguntan porque el nombre del usuario es PILAR, es por que esta no es mi PC :D)

Entre más datos, mejor. Entre más contenido podamos administrarle al clasificador, este sera más eficaz en sus clasificaciones. 

Este método puede ser usado para muchos propósitos: Clasificador de noticias, clasificador de tweets, hackeo de la CIA y del pentágono, entre otros. (Las ultimas 2 no están confirmadas, pero no perdemos nada intentándolo).

