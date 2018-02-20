"""
Dette programmet skal lage en ny regneklynge som heter abel. Regneklyngen sine noder skal hentes fra en fil som heter
regneklynge.txt. Programmet starter med aa lese den foerste linjen i tekstdokumentet som inneholder veriden for
maks antall noder per rack. Denne benyttets of aa instansiere regneklyngne. Deretter benyttes en metode som kan legge 
inn noder i regneklyngen for aa legge til alle nodene i tekstfilen. Til slutt i programmet skrives det ut litt statistikk
for aa sjekke at noder har blitt lagt inn korrekt. 

I dette programmet benyttes objektene Regneklynge, Rack og Node. Node inneholder kun antall prosessorer og minne. Et
rack har en bestemt antall noder, mens en Regneklynge kan bestaa av et uendelig antall rack. Regneklyngens metoder for aa 
beregne antall prosessorer og noder med nok minne delegeres videre ned til rack, som igjen benytter nodens metoder
for aa hente ut minne og antall prosessorer. 
"""

from regneklynge import Regneklynge

##Prosedyre som styrer programflyten
def main():

	#Aapner filen regneklynge.txt og leser foerst linje inn i variablen som holder maks antall noder
	with open("regneklynge.txt") as innFil:
		maksAntallNoderPerRack = int(innFil.readline())
		
		#Bruker maks antall noder som argument naar den nye regneklyngen Abel instansieres
		abel = Regneklynge(maksAntallNoderPerRack)
		
		#Itererer gjennom resten av linjene i regneklynge.txt og legger fortloepende til rack baser paa info i fil.
		for linje in innFil:
			splitLinje = linje.split()
			abel.leggTilFlereNoder(int(splitLinje[0]), int(splitLinje[1]), int(splitLinje[2]))
	
	#Sjekker antallet noder med nok minne
	print("Noder med minst 32GB: %i" % abel.noderMedNokMinne(32))
	print("Noder med minst 65GB: %i" % abel.noderMedNokMinne(64))
	print("Noder med minst 128GB: %i" % abel.noderMedNokMinne(128))
	print("Noder med minst 256GB: %i" % abel.noderMedNokMinne(256))
	print("Noder med minst 512GB: %i" % abel.noderMedNokMinne(512))
	print("Noder med minst 1024GB: %i" % abel.noderMedNokMinne(1024))
	print("Noder med minst 2048GB: %i" % abel.noderMedNokMinne(2048))
	print()
	
	#Skriver ut antallet prosessorer
	print("Antall prosessorer: %i" % abel.antProsessorer())
	
	#Skriver ut antall rack
	print("Antall rack: %i" % abel.antRack())
	
	
#Kaller metoden som styrer programflyten
main()