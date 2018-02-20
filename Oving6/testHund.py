#Program som tester klassen Hund. Programflyten blir styrt av hovedprogram. Hovedprogrammet benytter 
#metodene i Hund for aa faa en hund til aa gaa opp og ned i vekt med aa spise og springe.

##Prosedyre som skriver ut vekt og alder til en hund.
# @param hund er et Hundeobjekt som skal skrives ut
# @param navn er navnet til hunden
def skrivHund(hund, navn):
	print("%s er %i aar gammel og veier %ikg"%(navn, hund.hentAlder(), hund.hentVekt()))

##Prosedyre som styrer programflyten:
def hovedprogram():
	#Importerer klassen hund
	from hund import Hund
	
	#Lager ny hund som er 35aar og veier 50kg
	labbetuss = Hund(35, 50)
	
	#Skriver ut vekt og alder.
	skrivHund(labbetuss, "Labbetuss")
	
	#springer 6 ganger for aa redusere vekt.
	for i in range(6):
		print("Labbetuss springer")
		labbetuss.spring()

	#skriver ut vekt og alder
	skrivHund(labbetuss, "Labbetuss")
	
	#Spiser mat for aa gaa opp i vekt igjen
	print("Labbetuss spiser 3 mat")
	labbetuss.spis(4)
	
	#skriver ut vekt og alder
	skrivHund(labbetuss, "Labbetuss")
	
	#Springer 5 ganger for aa gaa ned i vekt
	for i in range(5):
		print("Labbetuss springer")
		labbetuss.spring()
	
	#skriver ut vekt og alder
	skrivHund(labbetuss, "Labbetuss")
	
	#Spiser litt mer for aa gaa opp i vekt
	print("Labbetuss spiser 10 mat")
	labbetuss.spis(10)
	
	#skriver ut vekt og alder
	skrivHund(labbetuss, "Labbetuss")
	
hovedprogram()