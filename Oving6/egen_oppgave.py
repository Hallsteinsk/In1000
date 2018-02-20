"""
Egen opppgave
Jeg hadde litt daarlig tid denne gangen saa jeg fulgte oppgaven foreslaatt i teksten slavisk: 

Skriv en klasse Person med en konstruktoer som tar imot navn og alder. I tillegg skal
konstruktoeren ha en tom liste hobbyer. Skriv en metode leggTilHobby som tar imot
en tekststreng og legger den til i hobbyer-listen. Skriv ogsaa en metode skrivHobbyer.
Denne metoden skal skrive alle hobbyene etter hverandre paa en linje. Gi deretter
Person-klassen en metode skrivUt som i tillegg til aa skrive ut navn og alder kaller paa
metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et Person-objekt
med informasjonen du faar. Deretter skal brukeren ved hjelp av en loekke faa legge til saa
mange hobbyer de vil. Naar brukeren ikke lenger oensker aa oppgi hobbyer skal
statistikk om brukeren skrives ut.
"""

class Person:
	#Klassevariabler
	navn = None
	alder = None
	hobbyer = []
	
	#Constructor
	def __init__(self, navn, alder):
		self.navn = navn
		while(True):
			try:
				self.alder = int(alder)
				break
			except:
				alder = input("Alder var ikke et heltall. Skriv inn alder paa nytt: ")
				
	
	##Metode som legger til en hobby i hobbylista
	# @param hobby er en tekststreng som legges til lista
	def leggTilHobby(self, hobby):
		self.hobbyer.append(hobby)
	
	##Metode som skriver ut hobbylista
	def skrivHobbyer(self):
		print("Hobbyer:")
		for linje in self.hobbyer:
			print("-%s" %linje)
			
	##Metode som skriver ut navn, alder i tillegg til hobbylista
	def skrivUt(self):
		print("Navn: %s" %self.navn)
		print("Alder: %s" %self.alder)
		self.skrivHobbyer()
		
	#Getters:
	def getNavn(self):
		return self.navn
		
	def getAlder(self):
		return self.alder


def hovedprogram():

	#Forklarer programmet til bruker og henter input til navn og alder
	print("Hei! Du skal naa skrive inn navn og alder:")
	navn = input("Skriv inn nanv: ")
	alder = input("Skriv inn alder: ")
	
	#Oppretter nytt personobjekt og bekrefter med beskjed til bruker.
	nyPerson = Person(navn, alder)
	print("Hei %s! Du er %i aar gammel." %(nyPerson.getNavn(), nyPerson.getAlder()))
	
	#Leser inn hobbyer fra bruker og legger dem til i hobbylista til personobjektet
	while(True):
		hobby = input("Skriv inn en hobby. (Skriv \"slutt\" for naar du er ferdig.)\n")
		if hobby.lower() == "slutt":
			break
		else:
			nyPerson.leggTilHobby(hobby)
	
	#Skriver ut statistikken til personobjektet
	print()
	print("Her er informasjonen om deg:")
	nyPerson.skrivUt()
	
hovedprogram()