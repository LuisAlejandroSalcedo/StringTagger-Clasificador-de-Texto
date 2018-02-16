import os
import requests
import pickle
from bs4 import BeautifulSoup as bs4

def getPageContent(url): # Función que devuelve todo el contenido HTML de una URL
	response = requests.get(url)
	return response.content
		
def html_to_text(html):
	soup = bs4(html, 'html.parser')
	return soup.get_text()

def getTextPage(url): # Función para extraer todo el texto del contenido HTML de la pagina 
	print("Aprendiendo de:", url)
	html = getPageContent(url)
	html_parsed = html_to_text(html)
	return html_parsed # Este texto sera mediante el cual se entrenara al clasificador