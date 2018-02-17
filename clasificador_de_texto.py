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
input()