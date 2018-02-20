##Beskrivelse av programflyt:
"""
Foers defineres funksjonen minFunksjon(), som ikke tar imot noen parametre. Deretter defineres prosedyren hovedprogram().
Hovedprogramprosedyren tar heller ikke imot noen parametre. Til slutt kaller programmet på hovedprogram(). 
Hovedprogram starter med å tildele en variabel 'a' 42 som verdi. Deretter tildelse 'b' verdiem 0. Programmet skriver saa ut
verdien til 'b' med bruk av print(). Etterpaa settes variablen 'b' sin lik verdien til 'a'. Saa proever programmet aa sette
'a' sin verdi til resultatet av minFunksjon(). minFunksjon() starter en for-loekke som skal kjoere to ganger. Inne i loekken settes 'c'
til 2 og blir skrevet ut foer 1 blir lagt til. 'b' blir satt til 10, saa proever programmet aa legge til verdien av 'a' til 'b',
foer b skrives ut. Variablen 'a' er ikke definert i minFunksjon sitt skop, saa at 'a' skal legges til 'b' kommer trolig til aa gaa daarlig...
Jeg regner med at programmet stopper her. Hadde 'a' vaert definert inne i minFunksjon() kunne hovedprogrammet fortsatt og skrevet ut 'a' og 'b'.

Etter at jeg testet dette programmet fikk jeg foelgende feilmelding:
"NameError: name 'a' is not defined."
Som antatt stoppet programmet der jeg trodde. 
"""
def minFunksjon():
	for x in range(2):
		print()
		c = 2
		print(c)
		c += 1
		b = 10
		b += a
		print(b)
	return(b)

def hovedprogram():
	a = 42
	b = 0
	print(b)
	b = a
	a = minFunksjon()
	print(b)
	print(a)
	
hovedprogram()