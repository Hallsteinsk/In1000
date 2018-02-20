class Node:

	#Constructor
	def __init__(self, minne, prosessorer):
		self._minne = minne
		self._prosessorer = prosessorer
	
	##Metode som returnerer antallet prosessorer i en node
	# @return antall prosessorer i noden
	def antProsessorer(self):
		return self._prosessorer
	
	##Metode som returnerer minnet til noden
	# @return minnet til noden
	def hentMinne(self):
		return self._minne