from node import Node

class Rack:

	#Constructor
	def __init__(self, maksNoder):
		self._nodeListe = []
		self._maksNoder = maksNoder
		
	##Metode som legger til en node i rack
	# @param minne er minnet som den nye noden skal has
	# @param prosessorer er antallet prosessorer noden skal ha
	def leggTilNode(self, minne, prosessorer):
		self._nodeListe.append(Node(minne, prosessorer))
	
	##Metode som returnerer True hvis det er plass til flere noder
	# @return bool som er True hvis det er plass til flere noder
	def ledigPlass(self):
		if len(self._nodeListe) < self._maksNoder:
			return True
		else: 
			return False
	
	##Metode som returnerer antallet prosessorer i racket
	# @return antallet prosessorer i rack
	def antProsessorer(self):
		total = 0
		for node in self._nodeListe:
			total += node.antProsessorer()
		return total
	
	##Metode som returnerer antallet noder med minst angitt minne
	# @param paakrevdMinne er minnet noden minst maa ha for aa bli medregnet i returverdien
	# @return antallet noder med minst paakrevdMinne
	def noderMedNokMinne(self, paakrevdMinne):
		antNoder = 0
		for node in self._nodeListe:
			if node.hentMinne() >= paakrevdMinne:
				antNoder += 1
		return antNoder