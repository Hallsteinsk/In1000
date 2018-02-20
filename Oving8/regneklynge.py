from rack import Rack

class Regneklynge:
	
	#Constructor: Setter maks antall noder per rack, og setter det foerste tomme racket inn i racklisten. 
	#Paa denne maaten er det altid minst et rack i listen.
	def __init__(self, maksNoder):
		self._rackListe = []
		self._maksNoder = maksNoder
		self._rackListe.append(Rack(self._maksNoder))
	
	
	##Metode som legger node til i rack.
	# @param minne er minnet til noed som skal legges til i rack
	# @param prosessorer er antallet prosessorer til noden som skal legges til i rack
	def leggTilNode(self, minne, prosessorer):
		if self._rackListe[-1].ledigPlass():
			self._rackListe[-1].leggTilNode(minne, prosessorer)
		else:
			self._rackListe.append(Rack(self._maksNoder))
			self._rackListe[-1].leggTilNode(minne, prosessorer)
	
	##Metode som legger til flere noder i rack
	# @param antall er antallet noder som skal legges til
	# @param minne er minnet til nodene som legges til
	# @param prosessorer er antallet prosessorer til nodene som skal legges til i rack
	def leggTilFlereNoder(self, antall, minne, prosessorer):
		for i in range(antall):
			self.leggTilNode(minne, prosessorer)
			
	##Metode som returnerer det totale antallet prosessorer i regneklyngen
	# @return antallet prosessorer i klyngen
	def antProsessorer(self):
		total = 0
		for rack in self._rackListe:
			total += rack.antProsessorer()
		return total
	
	##Metode som returnerer antall rack i regneklyngen
	# @return antallet rack. (Lengden av rackList)
	def antRack(self):
		return len(self._rackListe)
		
	##Metode som returnerer antallet noder med minst angitt minne
	# @param paakrevdMinne er minnet noden minst maa ha for aa bli medregnet i returverdien
	# @return antallet noder med minst paakrevdMinne
	def noderMedNokMinne(self, paakrevdMinne):
		antNoder = 0
		for rack in self._rackListe:
			antNoder += rack.noderMedNokMinne(paakrevdMinne)
		return antNoder