##Funksjon som returnerer summen av to parameter
# @param param1 det ene tallet som skal summeres
# @param param2 det andre tallet som skal summeres
# @return summen av param1 og param2
def addisjon(param1, param2):
	return param1 + param2

#Tester addisjon med aa kjoere selve funksjonen. 
sum = addisjon(3, 5)
print("Resultatet av addisjonsfunksjonen er %i" %sum)
print()
	
##Funksjon som returnerer et parameter subtrahert fra et annet
# @param param1 et tall
# @param param2 et tall som skal subtraheres fra param1
# @return resultatet av subtraksjonen
def subtraksjon(param1, param2):
	return param1 - param2

#Tester subtraksjon med assert
assert subtraksjon(5, 1) > 0
assert subtraksjon(1, 5) < 0
assert subtraksjon(-5, 3) < 0
assert subtraksjon(4, -6) > 0

##Funksjon som returnerer et parameter dividert paa et annet
# @param param1 et tall
# @param param2 et tall som skal divideres paa param1
# @return resultatet av subtraksjonen
def divisjon(param1, param2):
	assert(param2 != 0), "param2 er 0. Kan ikke del paa null."
	return param1 / param2

#Tester divisjon med assert
assert divisjon(5, 1) == 5
assert divisjon(-1, -5) > 0
assert divisjon(-15, 3) == -5
assert divisjon(4, -6) < 0

##Funksjon som beregner tommer om til cm
# @param antallTommer input i tommer.
# @return lengden i i cm. Flyttall.
def tommerTilCm(antallTommer):
	assert antallTommer != float
	assert (antallTommer > 0), "Tommer er ikke stoerre enn null" 
	return float(antallTommer * 2.54) 

##Prosedyre som benytter funksjonene over
def skrivBeregninger():
	#Henter inn tall fra bruker med exception handling. Gjoer alle tall om til float.
	print("Utregninger:")
	while(True):
		try:
			tall1 = float(input("Skriv inn tall 1: "))
			break
		except:
			print("Skriv inn et tall! Proev igjen.")
	while(True):
		try:
			tall2 = float(input("Skriv inn tall 2: "))
			break
		except:
			print("Skriv inn et tall! Proev igjen.")
	
	#Brukser funksjonene addisjon, subtraksjon og divisjon med tall innhentet fra bruker.
	print()
	print("Resultatet av summering er: %.1f" % addisjon(tall1, tall2))
	print("Resultatet av subraksjon er: %.1f" % subtraksjon(tall1, tall2))
	print("Resultatet av divisjon er: %.1f" % divisjon(tall1, tall2))

	#Henter inn et nytt tall fra bruker og bruker denne i konvertering til tommer
	print()
	print("Konvertering fra tommer til cm:")
	while(True):
		try:
			tall3 = float(input("Skriv inn et tall: "))
			break
		except:
			print("Skriv inn et tall! Proev igjen.")
	print("Resultatet av konvertering fra tommer til cm er: %.2f" % tommerTilCm(tall3))
#Debug
skrivBeregninger()
