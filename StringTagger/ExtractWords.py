import re, os
import pickle
from collections import defaultdict
from .getPage import getTextPage

def remove_urls(text): # Metodo para eliminar urls de los textos
	return re.sub("https?://[^\s]+","",text)
	
def getWords(text): # Obtenemos todo el texto y lo dividimos por palabras
	assert type(text) in (str,bytes)
	text = remove_urls(text)
	words = re.findall("[a-z]{2,}",text,re.I)	
	words = map(lambda x:x.lower(),words)
	return [word for word in words]

def wordFreq(text):	# Claculamos la frecuencia con la cual se repite una palabra
	words = getWords(text)
	count = defaultdict(int)
	for word in words:
		count[word] += 1	
	return count

