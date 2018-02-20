##Oppgavebeskrivelse:
#Gjorde en liten variasjon paa oppgaveforslag i oppgaveteksten.
#Skriv et beregninsprogram som leser inn fra filen 'egen_oppgave_innfil.txt'. Den inneholder navn og maal for en skredder.
#Filen inneholder ogsaa enhet paa maalene. Programmet skal finne ut om maal er oppgitt i tommer eller cm. Dersom det er
#tommer skal det omregnes til cm med tommerTilCm-funksjonen skrevet i 'regnefunksjoner.py'. Til slutt skal 
#listen med navn, maal og enhet skrives ut. 

#Min loesning:
#Benytter tommerTilCm for aa gjoere beregning fra tommer til cm. Lager ogsaa en funksjon som tar imot en hel liste og
#sjekker hvilken enhet maal er oppgitt i, og regner om dersom det er oppgitt i tommer. Lager en prosedyre som skriver ut 
#listen paa en ryddig maate. For aa faa til dette benyttes funksjonen finnLengsteOrd(). Der benyttes ordlengden til
#det lengste navnet i lista for aa formatere hele utskriften. Innlesing av data til liste skjer i funksjonen fyll liste, 
#som tar imot et filnavn og returnerer en liste med alle linjene i filen. Til slutt benyttes en hovedProgram-prosedyre for
#aa styre programflyten. Der defineres en dimensjonsListe som fylles med funksjonen fyllListe. Deretter blir maa omregnet
#med aa benytte tommerTilCmListe. Til slutt skrives ut listen med skrivListe. 


##Funksjon som beregner tommer om til cm
# @param antallTommer input i tommer.
# @return lengden i i cm. Flyttall.
def tommerTilCm(antallTommer):
	assert antallTommer != float
	assert (antallTommer > 0), "Tommer er ikke stoerre enn null" 
	return float(antallTommer * 2.54)

##Funksjon som sjekker om stoerrelser er i tommer eller cm. Dimensjoner endres til cm hvis det er tommer.
# @param dimensjonsListe er en listen som skal sjekks, og eventuelt konverteres til cm.
# @param return en liste med alle dimensjoner i cm.
#Spoersmaal til den som retter: Her kunne jeg godt tenkt meg aa brukt pekere, som i C. 
#Har python noe godt alternativ til dette? 
def tommerTilCmListe(dimensjonsListe):
	for element in dimensjonsListe:
		if element[2] == "tommer":
			element[1] = tommerTilCm(float(element[1]))
			element[2] = "cm"
		elif element[2] == "cm":
			element[1] = float(element[1])
	return dimensjonsListe
	
##Funksjon som fyller en liste med verdier fra en innfil.
# @param filNavn er filen som det skal leses fra.
# @param return en liste med data fra innfil
def fyllListe(filNavn):
	liste = []
	with open(filNavn, "r") as innFil:
		for linje in innFil:
			liste.append(linje.split())
	return liste

##Prosedyre som skriver ut en liste med ny linje for hvert element. 
#Benytter repr() formatering som beskrevet i python sin dokumentasjon: https://docs.python.org/3/tutorial/inputoutput.html
# @param innListe er listen som skal skrives ut til terminalen
def skrivListe(innListe):
	for element in innListe:
		print(repr(element[0]).rjust(finnLengsteOrd(innListe) + 2),repr(element[1]).rjust(5), repr(element[2]).rjust(4))

##Funksjon som finner lengden av det lengste ordet i dimensjonslisten
# @param innListe er listen hvor man skal lete etter det lengste ordet
# @return antall tegn i det lengste ordet. Integer
def finnLengsteOrd(innListe):
	lengst = 0
	for element in innListe:
		if len(element[0]) > lengst:	
			lengst = len(element[0])
	return lengst

##Prosedyre som inneholder programflyten.
def hovedProgram():
	#Definerer of fyller en dimensjonsliste med bruk av fyllListe()
	dimensjonsListe = fyllListe("egen_oppgave_innfil.txt")

	#Regner om alle dimensjoner til cm
	tommerTilCmListe(dimensjonsListe)

	#Skriver ut listen
	skrivListe(dimensjonsListe)

#Kjoerer hovedprogrammet
hovedProgram()