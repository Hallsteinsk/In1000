#Dette programmet leser presenterer bruker med en meny hvor man kan skrive inn tekststrenger og slaa dem sammen,
#eller skrive ut en liste med alle den sammenslaate strengene man har laget. Bruker kan selv avslutte med menyvalg.

##Funksjon som slaar sammen (konkatenerer) to strenger
# @param streng1 foerste streng.
# @param streng2 streng som skal slaas sammen med streng1
# @return den sammenslaate strengen
def slaaSammen(streng1, streng2):
	return streng1 + streng2

##Prosedyre som tar imot en liste og skriver ut hvert element
# @param liste er listen som skal skrives ut
def skrivUt(liste):
	for element in liste:
		print(element)

#Variablers som behoever instansiering		
mineOrd = []
brukerValg = "None"

#main loop som bruker interagerer med. 
while(brukerValg.lower() != "s"):
	
	brukerValg = input("Hva vil du gjoere? Skriv in bokstav:\ni: Legge sammen to tekststreng og lagre dem.\nu: Skriv ut alle tekststrenger\ns: Avslutt program.\n")
	
	if brukerValg.lower() == "i":
		brukerStreng1 = input("Skriv inn en tekststreng:\n")
		brukerStreng2 = input("Skriv inn en ny streng:\n")
		mineOrd.append(slaaSammen(brukerStreng1, brukerStreng2))
	elif brukerValg.lower() == "u":
		print("Utskrift av alle dine tekststrenger:\n")
		skrivUt(mineOrd)
		print()