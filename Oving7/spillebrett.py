from celle import Celle
from random import randint
import os

class Spillebrett:
	
	##Metode som "seeder" klassens rutenett med levende og doede celler
	def generer(self):
		for i in range(self._rader):
			for j in range(self._kolonner):
				rand = randint(0, 3)
				if rand == 3:
					self._rutenett[i][j].setLevende()
					
	##Constructor
	def __init__(self, rader, kolonner):
		self._rader = rader
		self._kolonner = kolonner
		#Opretter spillebrettet og fyller det med celler
		self._rutenett = [[Celle() for i in range(self._kolonner)]for j in range(self._rader)]
		#setter generasjonsnummer til 0
		self._generasjonsnummer = 0
		#Seeder spillebrett
		self.generer()
		#Prover aa finne systemnavn for aa lage en clearscreen-metode
		self._systemNavn = os.name
		try:
			if self._systemNavn == "nt":
				self._clearMetode = "win"
			else:
				self._clearMetode = "other"
		except:
			self._clearMetode = "other"
		
	##Metode som teller opp totalt antall levende celler
	# @return antall levende celler. int
	def tellLevende(self):
		levende = 0
		for i in range(self._rader):
			for j in range(self._kolonner):
				celle = self._rutenett[i][j]
				if celle.erLevende():
					levende += 1
		return levende
				
	##Metode som clearer terminalvinduet
	def clearScreen(self):
		if self._clearMetode == "win":
			os.system("cls")
		else:
			for h in range(50):
				print()
						
	##Metode som skriver ut spillebrettet til terminalen. Clearer skjermen foerst, skriver saa ut brettet. Til slutt skrives generasjonsnummer og antall levende celler.
	# @param mode er hvilken modus oppdateringen skjer. Dersom den er i modus "c" (kontinuerlig) skal en ekstra instruksjon skrives oeverst i bildet. Den har defaultverdi None.
	def tegnBrett(self, mode = None):
		self.clearScreen()
		if mode == "c":
			print("Trykk CTRL + C for aa avslutte kontinuerlig oppdatering.")
		for i in range(self._rader):
			for j in range(self._kolonner):
				print(self._rutenett[i][j].skrivTegn(), end="")
			print()
		print("Generasjon: %i - Antall levende Celler: %i" %(self._generasjonsnummer, self.tellLevende()))
	
	##Metode som finner antall levende naboer til en celle
	# @param rad er raden til cellen
	# @param kolonne er kolonnen til cellen
	# @return antallet levende naboceller, int
	def finnLevende(self, rad, kolonne):
		levende = 0
		naboliste = self.finnNabo(rad, kolonne)
		for nabo in naboliste:
			if nabo.erLevende():
				levende += 1
		return levende
		
			
	##Metode som finner alle naboene til en celle, og returnerer en liste med disse
	#Proevde paa en egen implementasjon, men den var veldig inspirert av koden i oppgaveteksten
	# @param rad er raden til cellen
	# @param kolonne er kolonnen til cellen. Sammen med rad kan man se paa en spesifikk celle.
	# @return en liste med alle naboene til cellen med koordinatene rad og kolonne. 
	def finnNabo(self, rad, kolonne):
		naboer = []
		for i in range(-1, 2):
			for j in range(-1, 2):
				naboRad = rad + i
				naboKolonne = kolonne + j
				if(naboRad == rad and naboKolonne == kolonne) != True:
					if(naboRad < 0 or naboKolonne < 0 or naboRad > self._rader -1 or naboKolonne > self._kolonner -1) != True:
						naboer.append(self._rutenett[naboRad][naboKolonne])
		return naboer
	
	##Metode som beregner neste generasjon av celler
	def oppdater(self):
		skalBliLevende = []
		skalBliDoed = []
		
		#Gaar gjennom alle celler og rutenett og finner antallet levende naboer
		for i in range (self._rader):
			for j in range(self._kolonner):
				levendeNaboer = self.finnLevende(i,j)
				celle = self._rutenett[i][j]
				#Bruker spillets regler for aa bestemme om en celle skal bli levende eller doed etter oppdatering
				if celle.erLevende():
					if levendeNaboer < 2 or levendeNaboer > 3:
						skalBliDoed.append(celle)
				elif celle.erLevende() == False:
					if levendeNaboer == 3:
						skalBliLevende.append(celle)
		
		#Setter status til celler til levende eller doed
		for celle in skalBliLevende:
			celle.setLevende()
		for celle in skalBliDoed:
			celle.setDoed()
		
		#Oppdaterer generasjonsnummer
		self._generasjonsnummer += 1
		
	
	
	
	
	
	
			
			
