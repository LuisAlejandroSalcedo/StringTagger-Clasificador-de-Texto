"""
Uso sencillo de "StringTagger" para la clasificación de texto.
"""

__author__ = "Luis Salcedo" 

from StringTagger.StringClf import Classifier
from StringTagger.getPage import getTextPage

training_data = { # Entrenamos al clasificador con textos de paginas webs
# Estas son las clasificaciones en las cuales el clasificador clasificara el texto proporcionado
	"Ciencia":[
		'https://es.wikipedia.org/wiki/Ciencia', # Entrenamos al clasificador con paginas de wikipedia.
		'https://es.wikipedia.org/wiki/Qu%C3%ADmica' # Puedes escoger la pagina de tu preferencia (Ej Articulos de TheNewYorkTimes)
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

clf = Classifier() # Instancia del clasifica

for category,urls in training_data.items(): # Entrenamos al clasificador con el contenido de cada pagina
	for url in urls:
		clf.train(getTextPage(url),category) # El metodo "getTextPage", recive como parametro una url para extraer su texto

# Iniciamos el proceso de clasificación con el metodo "String"
# Solo le pasamos como argumento el texto que deseamos clasificar
clas = clf.String("El agua es una molécula simple: dos átomos de hidrógeno unidos a uno de oxígeno.") 
print('\n')
print("Clasificación del Texto: %s" % clas)