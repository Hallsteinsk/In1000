#Oppgave 1
#Deloppgave 1: Lager en funksjon som adderer to heltall. Kaller funksjonen to ganger med selvvalgte tall.

def adder(tall1, tall2):
	return tall1 + tall2

resultat1 = adder(2, 8)
resultat2 = adder(3, 3)

print("Resultat nummer 1: %i" % resultat1) 
print("Resultat nummer 2: %i" % resultat2) 

#Deloppgave 2 og 3: Funksjon som teller forekomsten av en bokstav i en streng. Streng og bokstav leses inn fra bruker
#Deloppgave 2 er selve funksjonaliteten, mens i deloppgave 3 er dette omgjort til en egene funksjon.
def tellForekomst(minTekst, minBokstav):
	forekomst = 0
	for char in tekstStreng:
		if char == bokstav:
			forekomst += 1
	return forekomst

tekstStreng = input("Skriv inn en liten tekst: ")
bokstav = input("Skriv inn en bokstav: ")

forekomst = tellForekomst(tekstStreng, bokstav)
print("Bokstaven \"%c\" forekommer %i ganger i teksten \"%s\"." % (bokstav, forekomst, tekstStreng))
