##Funksjon som tar imot en liste med heltall og reurnerer gjennomsnittet av den
# @param liste listen som inneholder heltall hvor gjennomsnittet skal beregnes av. 
# @return gjennomsnittet av liste. Returverdien er et flyttall
def gjennomsnitt(liste):
	sum = 0
	antallElement = 0
	for element in liste:
		sum += element
		antallElement += 1
	return float(sum/antallElement)

#Aapner fil og leser data inn i liste
tempListe = []
with open("temperatur.txt") as innFil:
	for linje in innFil:
		tempListe.append(int(linje))

#Bruker funksjonen gjennomsnitt for aa skrive ut gjennomsnittstemp.
print("Gjennomsnittstemperatur er: %.1f" %gjennomsnitt(tempListe))