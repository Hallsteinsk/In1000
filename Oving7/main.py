"""
Dette er et program som spiller Conways Game of Life. Klassene spillebrett og celle benyttes for 
aa gejnnomfoere dette. Foerst skal bruker bestemme stoerrelse paa brett, 
deretter genereres startsituasjonen. Etter den er generert kan bruker manuelt oppdatere med aa
bruke enter-tasten, eller la programmet automatisk oppdatere seg. Jeg har ikke funnet noe elegant
maate aa avslutte kontinuerlig oppdatering, saa man maa bruke CTRL + C for aa bryte ut av den loekka...
Bruker kan velge aa avslutte hele programmet ogsaa fra menyen.
"""

#Imports
from spillebrett import Spillebrett
import time

##Prosedyre som kontrollerer programflyten
def main():
	#Lar bruker bestemme stoerrelsen paa spillebrettet, men feilsjekking.
	print("Du skal naa spille Conways Game of Life. Bestem stoerrelsen paa spillebrettet:")
	while(True):
		try:
			stoerrelse = int(input("Skriv inn stoerrelsen: "))
			break
		except ValueError:
			print("Spillebrettets dimensjoner maa vaere heltall. Proev igjen:")
	
	#Begrenser stoerrelsen paa spillebrettet til 79, for da blir det ikke for stort i windows sitt terminalvindu. 
	if stoerrelse > 79:
		stoerrelse = 79
	
	#Generer det forerste spillebrettet
	nyttSpill = Spillebrett(stoerrelse, stoerrelse)
	nyttSpill.tegnBrett()
	
	#Menyloekke som lar bruker velge mellom manuell eller automatisk oppdatering av spillebrett
	while(True):
		inn = input("Trykk enter for aa oppdater spillebrett.\nTrykk q og saa enter for aa stoppe.\nTrykk c for aa kjoere kontinuerlig oppdatering. (Trykk CTRL + C for aa avslutte)")
		if inn.lower() == "q":
			break
		elif inn.lower() == "c":
			try:
				while(True):
					nyttSpill.oppdater()
					nyttSpill.tegnBrett("c")
					time.sleep(0.75)
					
			except KeyboardInterrupt:
				pass
		else:
			nyttSpill.oppdater()
			nyttSpill.tegnBrett()

#Kjoer main loop
main()