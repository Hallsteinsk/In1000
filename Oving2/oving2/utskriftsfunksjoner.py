#Deloppgave 1 er innbakt i deloppgave 2

#Deloppgave 2
def brukerKommunikasjon(): #Deffinerer ny funksjon. 
	navn = input("Skriv inn navn: ") #Lagrer brukerinput paa navn, 
	bosted = input("Hvor kommer du fra? ") #og bosted. 
	print("Hei, " + navn + "! Du kommer fra " + bosted + ".\n") #"Legger sammen" strengene i print-funksonen

for i in range (0,3): #Lager for-loop som kjoerer funksjonen 3 ganger. 
	brukerKommunikasjon()