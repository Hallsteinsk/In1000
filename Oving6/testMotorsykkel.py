##Program som henter inn klassen motorsykkel og tester metodene i den klassen. Det oprettes 3 motorsykkelobjekter, som
#skrives ut. Deretter kjoerer vi en tur med en av motorsyklene, foer vi tester om kilometerstanden har oekt.
#Jeg oppretter ogsaa en liste som inneholder alle motorsykkel-objektene. Dette gjoer det litt lettere aa iterere over alle objektene
#i forbindelse med f.eks en utskrift. 

from motorsykkel import Motorsykkel

##Prosedyre som styrer programflyten
def hovedporgram():
	#Instansierer tre nye motorsykkler
	motorsykkelEn = Motorsykkel("Yamaha", "12345", 40.5)
	motorsykkelTo = Motorsykkel("BMW", "SWE-123", 7.89)
	motorsykkelTre = Motorsykkel("Ford","Hei-99" , 0)
	
	#Lager en liste med alle motorsykkel-objektene for enklere haandtering.
	motorsykkelListe = [motorsykkelEn, motorsykkelTo, motorsykkelTre]
	
	#Skriver ut alle objektene
	for motorsykkel in motorsykkelListe:
		motorsykkel.skrivUt()
	
	#Kjoerer det siste objektet 10km. (Oeker km.stand med 10)
	motorsykkelListe[2].kjor(10)
	
	#Kontrollerer at km.standend har oekt
	print("Kilometerstand paa den tredje motorsyklen er: %.1f" % motorsykkelListe[2].hentKilometerstand())
	
#Kjoerer hovedporgramet
hovedporgram()
	