import math, re
from collections import defaultdict
from fractions import Fraction
from .ExtractWords import getWords, wordFreq

class Classifier(object):
	def __init__(self):
		super(Classifier, self).__init__()
		self.classes = defaultdict(lambda : defaultdict(int))
		self.SamplesTotal = 0		
		self.vocab = {}

	def train(self,obj,className): # Entrenamos al clasificador
		frequents = None
		if isinstance(obj,str) or isinstance(obj,bytes):
			frequents = wordFreq(obj)			
		elif isinstance(obj,dict):
			frequents = obj			 
		else:
			raise Exception("El objeto debe ser una cadena de texto o una palabra frecuente.")			
		for word, freq in frequents.items():	
			self.classes[className][word] += freq

	def allWords(self):
		vocab = set()
		for freqMaps in self.classes.values():
			vocab = vocab.union(freqMaps.keys())
		return sorted(vocab)
			
	def computeProb(self,obj,className): # Parte logica
		words = None
		if type(obj) in (str,bytes):		
			words = getWords(obj)
		else:
			words = obj
		numWords = sum(self.classes[className].values())
		logSum = 0
		for word in words:
			freq = self.classes[className][word] + 1
			prob = Fraction(freq,numWords)
			logSum += math.log(prob)
		return logSum
	
	def String(self,obj,verbose=False): # Clasificar cadena de texto
		probs = {}
		for className in self.classes:
			probs[className] = self.computeProb(obj,className)
		
		highestClass = sorted(probs,key=probs.get)[-1]
		highest = probs[highestClass]
		if verbose:
			print(probs)
		return highestClass # Clase más alta