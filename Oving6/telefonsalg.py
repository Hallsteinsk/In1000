#Dette er et program som leser salgsstatistikk fra en tekstfil og gjoer beregninger paa disse. Programmet finner
#selger med flest salg, totalt antall salg, gjennomsnittsalg per salgsperson og hvor mange salgspersoner som er aktive.

##Funksjon som leser inn data fra en fil og returnere en ordbok.
# @param filnavn er filnavnet paa filen som det skal leses fra
# @return en ordbok med informasjonen i filen fil
def innlesing(filnavn):
	ordBok = {}
	with open(filnavn, "r") as innFil:
		for linje in innFil:
			linjeSplit = linje.split(" ")
			ordBok[linjeSplit[0]] = int(linjeSplit[1])
	return ordBok

##Funksjon som summerer totalt antall salg i en ordbok
# @param salgsStatistikk er ordboken som inneholder salg
# @return antall salg totalt. int.
def totaltAntallSalg(salgsStatistikk):
	totaltAntallSalg = 0
	for noekkel in salgsStatistikk:
		totaltAntallSalg += salgsStatistikk[noekkel]
	return int(totaltAntallSalg)
	
##Funksjon som retrunerer gjennomsnittsalg per person i ordboken som inneholder salgsstatistikk
# @param salgsStatistikk er ordboken med antall salg
# @return gjennomsnittsalg. Float.
def gjennomsnittSalg(salgsStatistikk):
	return totaltAntallSalg(salgsStatistikk)/len(salgsStatistikk)

##Prosdeyre som finner den personen som har hatt flest salg denne maaneden.
# @param ordBok er ordboken prosedyren leter gjennom for aa finne den personen som har hatt flest salg
def maanedensSalgsperson(salgsStatistikk):
	flestSalg = -1
	noekler = salgsStatistikk.keys()
	for noekkel in noekler:
		if salgsStatistikk[noekkel] > flestSalg:
			besteSalgsperson = noekkel
			flestSalg = salgsStatistikk[noekkel]
	print(besteSalgsperson + " er den beste selgeren med hele " + str(flestSalg) + " salg!")
	
##Prosdeyre som skriver ut ordboken. Brukes ikke i den ferdige koden, men jeg brukte den under debugging.
# @param ordBok er ordboken som skal skrives ut
def skrivOrdbok(ordBok):
	noekler = ordBok.keys()
	for enhet in noekler:
		print(enhet + ": " + str(ordBok[enhet]))

##Prosdeyre som inneholder programflyten
def hovedprogram():
	salgsStatistikk = innlesing("salgstall.txt")
	maanedensSalgsperson(salgsStatistikk)
	
	print()
	print("Aktive selgere denne maaneden: %i" % len(salgsStatistikk))
	print("Totalt antall salg denne maaneden: %i" % totaltAntallSalg(salgsStatistikk))
	print("Gjenomsnittlig antall salg per salgsperson: %.2f" % gjennomsnittSalg(salgsStatistikk))

hovedprogram()

