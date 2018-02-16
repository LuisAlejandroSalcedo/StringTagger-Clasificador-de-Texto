import re, os
import pickle
from collections import defaultdict
from .getPage import getTextPage

def remove_urls(text):
	return re.sub("https?://[^\s]+","",text)
	
def getWords(text):
	assert type(text) in (str,bytes)
	text = remove_urls(text)
	words = re.findall("[a-z]{2,}",text,re.I)	
	#make everything lowercase.
	words = map(lambda x:x.lower(),words)
	#filter out stop words
	return [word for word in words]

def wordFreq(text):	
	words = getWords(text)
	count = defaultdict(int)
	for word in words:
		count[word] += 1	
	return count

