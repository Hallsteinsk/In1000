#Oppgave 1, lister.py

#Deloppgave 1
#Lager ny liste (minListe), legger til 4 bakerst i listen og skriver ut foerste og tredje elemnt.
minListe = [1, 2, 3]
minListe.append(4)
print("Foerste element:", minListe[0])
print("Tredje element:", minListe[2])

#Deloppgave 2
#Lager en tom liste (nyListe) som fylles med input fra bruker i en for loop
nyListe = []
print("Du skal naa skrive inn 4 navn.")
for i in range (0,4):
	nyListe.append(input("Skriv inn navn nr " + str(i + 1) + ":\n"))

#Deloppgave 3
#Sjekker om navnet mitt ligger i nyListe og skriver ut passende reaksjon i foelge oppgaveteksten
if "Hallstein" in nyListe:
	print("Du husket meg!")
else:
	print("Glemte du meg?")

#Deloppgave 4	
sammenListe = minListe + nyListe
print(sammenListe)
sammenListe.remove(sammenListe[7])
sammenListe.remove(sammenListe[6])
print(sammenListe)
