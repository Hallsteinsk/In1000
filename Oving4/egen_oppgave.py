#Oppgave 5
#Egen oppgave. Velger aa bruke eksempel i oppgaveteksten. Lag et program som lar bruker holde styr paa, legge til
#skrive ut venners bursdag.

#Min loesening:
#Lager en venneklasse som inneholder navn og bursdag. Lager ogsaa en venneAdmin-klasse som holder styr paa venner. 
#Deretter lager jeg en main som skriver ut en meny som lar bruker velge om man skal legge til venn, slette venn, eller skrive ut lista.

#Venneobjekt
class Venn:
	navn = None
	bursdag = None

	#Constructor
	def __init__(self, navn, bursdag):
		self.navn = navn
		self.bursdag = bursdag
	
#Vennelisteobjekt. Klasse som inneholder liste med venner og funksjoner som administrerer denne.
class VenneListeAdmin:
	venneListe = []
	
	#Constructor
	def __init__(self):
		return None
	
	#Funksjon som legger til en venn i lista
	def leggTilVenn(self, navn, bursdag):
		self.venneListe.append(Venn(navn, bursdag))
	
	#Funksjon som fjerner en navngitt venn i lista
	def slettVenn(self, navn):
		index = 0
		for venn in self.venneListe:
			if venn.navn.lower() == navn.lower():
				self.venneListe.pop(index)
				return True
			index += 1
		return False
	
	#Funksjon som skriver ut hele vennelista
	def printVenneListe(self):
		print()
		for venn in self.venneListe:
			print(venn.navn + " har bursdag " + venn.bursdag + ".")
		print()

#Funksjon som skriver ut meny, og returnerer brukers alternativ
def printMeny():
	return input("Skriv inn det tallet som beskriver hva du vil gjoere\nMeny:\n1: Legg til venn.\n2: Slett venn.\n3: Skriv ut venneliste.\n9: Avslutt programmet.\n")
	

#Program som benytter Venn og VenneListeAdmin for aa holde styr paa venners bursdag:

#Instansierer venneliste
venneListe = VenneListeAdmin()

#Main loop
while(True):
	
	alternativ = printMeny()
	
	if alternativ == "1":
		print("\nDu skal naa skrive inn navn og bursdag paa dine venner.\nSkriv inn \"slutt\" i navnefelt hvis du har skrevet inn alle dine venner.")
		while(True):
			navn = input("Skriv inn navn paa din venn: ")
			if navn.lower() == "slutt":
				print()
				break
			bursdag = input("Skriv inn bursdagsdato paa din venn: ")
			venneListe.leggTilVenn(navn, bursdag)
			
	elif alternativ == "2":
		venneListe.slettVenn(input("\nSkriv inn navnet paa den vennen du vil slette fra vennlista di: "))
	
	elif alternativ == "3":
		venneListe.printVenneListe()
	
	elif alternativ == "9":
		break
	
	else:
		print("Du skrev inn en ugyldig verdi. Proev igjen.\n")
